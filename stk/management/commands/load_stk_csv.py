import csv
import datetime
import logging
import pytz

from django.core.management.base import BaseCommand
from django.db import transaction

from stk.models import STKInspection, Vehicle

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('input_path', type=str, nargs=1)

    def handle(self, *args, **options):
        fieldnames = [
            'STK', 'DrTP', 'VIN', 'DatKont', 'TZn', 'TypMot', 'DrVoz',
            'ObchOznTyp', 'Ct', 'DatPrvReg', 'Km', 'ZavA', 'ZavB', 'ZavC',
            'VyslSTK', 'VyslEmise'
        ]
        with open(options['input_path'][0], 'r') as csv_f:
            reader = csv.DictReader(csv_f, fieldnames=fieldnames)
            next(reader) # skip header
            for i, chunk in enumerate(self.gen_rows(reader), start=1):
                logger.debug(f'Processing chunk {i} of size {len(chunk)}')
                with transaction.atomic():
                    for row in chunk: 
                        vehicle = self.create_vehicle(row)
                        inspection = self.create_inspection(row, vehicle)
                logger.debug('Saving to DB...')

    def gen_rows(self, reader):
        rows = []
        for i, row in enumerate(reader, start=1):
            rows.append(row)
            if i % 10000 == 0:
                yield rows
                rows = []
        yield rows

    def create_vehicle(self, row):
        return Vehicle.objects.create(
            vehicle_vendor=row['TZn'],
            vehicle_model=row['ObchOznTyp'],
            vehicle_type=row['DrVoz'],
            vehicle_category=row['Ct'],
            engine_type=row['TypMot'],
            vin=row['VIN'],
            km=row['Km'],
            first_registration_date=datetime.datetime.strptime(row['DatPrvReg'], '%Y-%m-%dT%H:%M:%S').date()
        )

    def create_inspection(self, row, vehicle):
        preprocessed_time_str = row['DatKont'][:-4] if len(row['DatKont']) == 23 else row['DatKont']
        return STKInspection.objects.create(
            stk_id=row['STK'],
            inspection_type=row['DrTP'],
            inspection_time=datetime.datetime.strptime(preprocessed_time_str, '%Y-%m-%dT%H:%M:%S').replace(
                tzinfo=pytz.UTC
            ),
            zav_a=row['ZavA'],
            zav_b=row['ZavB'],
            zav_c=row['ZavC'],
            inspection_result=row['VyslSTK'],
            emission_result=row['VyslEmise'],
            vehicle=vehicle
        )

import logging
import pandas as pd

from django.core.management.base import BaseCommand

from stk.models import Station

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('input_path', type=str, nargs=1)

    def handle(self, *args, **options):
        df = pd.read_excel(options['input_path'][0])
        for col in df.columns:
            df[col] = df[col].astype(str)

        for i, row in df.iterrows():
            Station.objects.create(
                stk_id=row['STK č.'].replace('.', '').strip(),
                authorization=row['Opravnenia'].strip(),
                zip_code=row['PSČ'].strip(),
                city=row['Město'].strip(),
                address=row['Ulice'].strip(),
                operator=row['Provozovatel STK'].strip(),
                tel_number=row['Telefon'].strip(),
                email=row['E-mail'].strip(),
                region=row['Kraj'].strip()
            )

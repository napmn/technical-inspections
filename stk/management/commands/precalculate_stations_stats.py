import itertools
import logging
import pandas as pd

from django.core.management.base import BaseCommand

from stk.enums import InspectionResult, InspectionTypeNormalized
from stk.models import Station, STKInspection, PrecalculatedStatistic, InspectionTypeStatistic

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        for station in Station.objects.exclude(region=None):
            logger.debug(f'Processing station {station}')

            inspections_in_station = STKInspection.objects.filter(station=station)
            eligible = inspections_in_station.filter(inspection_result=InspectionResult.ELIGIBLE).count()
            ineligible = inspections_in_station.filter(inspection_result=InspectionResult.INELIGIBLE).count()
            partially_eligible = inspections_in_station.filter(
                inspection_result=InspectionResult.PARTIALLY_ELIGIBLE
            ).count()

            total = eligible + ineligible + partially_eligible
            if total != 0:
                station.number_of_inspections = total
                station.pass_rate = (eligible + partially_eligible) / total
                station.save()

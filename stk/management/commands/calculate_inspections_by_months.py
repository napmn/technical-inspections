import itertools
import logging

from django.core.management.base import BaseCommand

from stk.enums import InspectionResult, InspectionTypeNormalized
from stk.models import Station, STKInspection, PrecalculatedStatistic, InspectionTypeStatistic, InspectionsInMonth

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        regions = Station.objects.exclude(region=None).values_list('region', flat=True).distinct()
        regions_and_all = list(regions) + [None]

        for region in regions_and_all:
            logger.debug(f'Processing region {region}')
            ps = PrecalculatedStatistic.objects.get(region=region)
            if region is None:
                # we dont want to include stations that dont have assigned region
                stations = Station.objects.exclude(region=None)
            else:
                stations = Station.objects.filter(region=region)

            inspections_in_region = STKInspection.objects.filter(station__in=stations)

            for month in range(1, 13):
                inspections = inspections_in_region.filter(inspection_time__month=month)
                passed = inspections.filter(
                    inspection_result__in=[InspectionResult.ELIGIBLE, InspectionResult.PARTIALLY_ELIGIBLE]
                ).count()
                not_passed = inspections.filter(
                    inspection_result=InspectionResult.INELIGIBLE
                ).count()

                InspectionsInMonth.objects.create(
                    precalculated_statistic=ps,
                    month=month,
                    passed=passed,
                    not_passed=not_passed,
                )

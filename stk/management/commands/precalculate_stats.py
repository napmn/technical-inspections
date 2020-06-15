import itertools
import logging
import pandas as pd

from django.core.management.base import BaseCommand

from stk.enums import InspectionResult, InspectionTypeNormalized
from stk.models import Station, STKInspection, PrecalculatedStatistic, InspectionTypeStatistic

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        regions = Station.objects.exclude(region=None).values_list('region', flat=True).distinct()
        regions_and_all = list(regions) + [None]
        for region in regions_and_all:
            logger.debug(f'Calculating statistics for region {region}')
            if region is None:
                stations = Station.objects.all()
            else:
                stations = Station.objects.filter(region=region)
            number_of_stations = stations.count()

            inspections_in_region = STKInspection.objects.filter(station__in=stations)
            number_of_inspections = inspections_in_region.count()

            eligible = inspections_in_region.filter(inspection_result=InspectionResult.ELIGIBLE).count()
            ineligible = inspections_in_region.filter(inspection_result=InspectionResult.INELIGIBLE).count()
            partially_eligible = inspections_in_region.filter(
                inspection_result=InspectionResult.PARTIALLY_ELIGIBLE
            ).count()

            precalculated_statistic = PrecalculatedStatistic.objects.create(
                region=region,
                number_of_stations=number_of_stations,
                number_of_inspections=number_of_inspections,
                eligible=eligible,
                ineligible=ineligible,
                partially_eligible=partially_eligible
            )

            inspection_types = [x for x,y in InspectionTypeNormalized.CHOICES]
            for inspection_type, repeated in itertools.product(*[inspection_types, [True, False]]):
                logger.debug(
                    f'Creating inspection type statistic for region: {region}, inspection type:{inspection_type}, '
                    f'repeated: {repeated}'
                )
                number_of_inspections = STKInspection.objects.filter(
                    inspection_type=inspection_type, repeated=repeated
                ).count()
                InspectionTypeStatistic.objects.create(
                    precalculated_statistic=precalculated_statistic,
                    inspection_type=inspection_type,
                    repeated=repeated,
                    number_of_inspections=number_of_inspections
                )

import logging
import pandas as pd

from django.core.management.base import BaseCommand

from stk.enums import InspectionType, InspectionTypeNormalized
from stk.models import STKInspection

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        count = 0
        already_normalized_types = [
            InspectionType.TSK, InspectionType.ADR, InspectionType.REGULAR, InspectionType.BEFORE_APPROVAL,
            InspectionType.BEFORE_REGISTRATION, InspectionType.ORDERED_TECH_INSPECTION,
            InspectionType.EVIDENCE_CONTROL, InspectionType.CUSTOMER_REQUESTED
        ]
        inspections_to_normalize = STKInspection.objects.exclude(inspection_type__in=already_normalized_types)
        total = inspections_to_normalize.count()

        for inspection in inspections_to_normalize:
            count += 1
            if count % 10000 == 0:
                logger.debug(f'Processing inspection {count}/{total}')

            if inspection.inspection_type in [InspectionType.TSK_REPEATED, InspectionType.TSK_REPEATED_AFTER_DN]:
                inspection.inspection_type = InspectionTypeNormalized.TSK
                inspection.repeated = True
            elif inspection.inspection_type == InspectionType.ADR_REPEATED:
                inspection.inspection_type = InspectionTypeNormalized.ADR
                inspection.repeated = True
            elif inspection.inspection_type == InspectionType.REPEATED:
                inspection.inspection_type = InspectionTypeNormalized.REGULAR
                inspection.repeated = True
            elif inspection.inspection_type == InspectionType.BEFORE_APPROVAL_REPEATED:
                inspection.inspection_type = InspectionTypeNormalized.BEFORE_APPROVAL
                inspection.repeated = True
            elif inspection.inspection_type == InspectionType.BEFORE_REGISTRATION_REPEATED:
                inspection.inspection_type = InspectionTypeNormalized.BEFORE_REGISTRATION
                inspection.repeated = True

            inspection.save()

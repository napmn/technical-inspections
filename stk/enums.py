class InspectionType:
    TSK_REPEATED = 'TSK - Opakovaná'
    ORDERED_TECH_INSPECTION = 'Nařízená technická prohlídka'
    REGULAR = 'pravidelná'
    EVIDENCE_CONTROL = 'Evidenční kontrola'
    TSK = 'Technická silniční kontrola'
    ADR = 'ADR'
    REPEATED = 'opakovaná'
    TSK_REPEATED_AFTER_DN = 'TSK - Opakovaná po DN'
    BEFORE_APPROVAL = 'Před schvál. tech. způsob. vozidla'
    ADR_REPEATED = 'ADR - opakovaná'
    BEFORE_APPROVAL_REPEATED = 'Před schvál. tech. způsob. vozidla - opakovaná'
    BEFORE_REGISTRATION_REPEATED = 'Před registrací - opakovaná'
    BEFORE_REGISTRATION = 'Před registrací'
    CUSTOMER_REQUESTED = 'Na žádost zákazníka'

    CHOICES = (
        (TSK_REPEATED, 'TSK - Opakovaná'),
        (ORDERED_TECH_INSPECTION, 'Nařízená technická prohlídka'),
        (REGULAR, 'pravidelná'),
        (EVIDENCE_CONTROL, 'Evidenční kontrola'),
        (TSK, 'Technická silniční kontrola'),
        (ADR, 'ADR'),
        (REPEATED, 'opakovaná'),
        (TSK_REPEATED_AFTER_DN, 'TSK - Opakovaná po DN'),
        (BEFORE_APPROVAL, 'Před schvál. tech. způsob. vozidla'),
        (ADR_REPEATED, 'ADR - opakovaná'),
        (BEFORE_APPROVAL_REPEATED, 'Před schvál. tech. způsob. vozidla - opakovaná'),
        (BEFORE_REGISTRATION_REPEATED, 'Před registrací - opakovaná'),
        (BEFORE_REGISTRATION, 'Před registrací'),
        (CUSTOMER_REQUESTED, 'Na žádost zákazníka')
    )


class InspectionTypeNormalized:
    TSK = 'Technická silniční kontrola'
    ADR = 'ADR'
    REGULAR = 'Pravidelná'
    BEFORE_APPROVAL = 'Před schvál. tech. způsob. vozidla'
    BEFORE_REGISTRATION = 'Před registrací'
    ORDERED_TECH_INSPECTION = 'Nařízená technická prohlídka'
    EVIDENCE_CONTROL = 'Evidenční kontrola'
    CUSTOMER_REQUESTED = 'Na žádost zákazníka'

    CHOICES = (
        (TSK, 'Technická silniční kontrola'),
        (ADR, 'ADR'),
        (REGULAR, 'Pravidelná'),
        (BEFORE_APPROVAL, 'Před schvál. tech. způsob. vozidla'),
        (BEFORE_REGISTRATION, 'Před registrací'),
        (ORDERED_TECH_INSPECTION, 'Nařízená technická prohlídka'),
        (EVIDENCE_CONTROL, 'Evidenční kontrola'),
        (CUSTOMER_REQUESTED, 'Na žádost zákazníka')
    )


class InspectionResult:
    ELIGIBLE = 'Způsobilé'
    INELIGIBLE = 'Nezpůsobilé'
    PARTIALLY_ELIGIBLE = 'Částečně způsobilé'

    CHOICES = (
        (PARTIALLY_ELIGIBLE, 'Způsobilé'),
        (INELIGIBLE, 'Nezpůsobilé'),
        (PARTIALLY_ELIGIBLE, 'Částečně způsobilé')
    )


class EmissionResult:
    SATISFIES = 'vyhovuje'
    NOT_SATISFIES = 'nevyhovuje'
    PARTIALLY_SATISFIES = 'částečně vyhovuje'

    CHOICES = (
        (SATISFIES, 'vyhovuje'),
        (NOT_SATISFIES, 'nevyhovuje'),
        (PARTIALLY_SATISFIES, 'částečně vyhovuje')
    )

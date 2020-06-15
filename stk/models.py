
from django.contrib.postgres.indexes import HashIndex
from django.db import models

from stk.enums import InspectionType, InspectionTypeNormalized, InspectionResult, EmissionResult


class Vehicle(models.Model):
    vehicle_vendor = models.CharField(max_length=255, db_index=True) # TZn
    vehicle_model = models.CharField(max_length=255) # ObchOznTyp
    vehicle_vendor_model = models.CharField(max_length=512, blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, db_index=True) # DrVoz
    vehicle_category = models.CharField(max_length=255) # Ct

    engine_type = models.CharField(max_length=255) # TypMot
    vin = models.CharField(max_length=255) # VIN
    km = models.IntegerField() # Km

    first_registration_date = models.DateField(null=True, blank=True) # DatPrvReg

    class Meta:
        indexes = [
            HashIndex(fields=('vehicle_vendor_model',))
        ]

    def __str__(self):
        return f'{self.vehicle_vendor} - {self.vehicle_model} - {self.vehicle_type}'

    def save(self, *args, **kwargs):
        if not self.vehicle_vendor_model:
            self.vehicle_vendor_model = f'{self.vehicle_vendor} {self.vehicle_model}'

        super().save(*args, **kwargs)

class STKInspection(models.Model):
    station = models.ForeignKey('stk.Station', to_field='stk_id', null=False, blank=False, on_delete=models.CASCADE)
    inspection_type = models.CharField(max_length=255, choices=InspectionTypeNormalized.CHOICES, db_index=True) # DrTP
    repeated = models.BooleanField(default=False)
    inspection_time = models.DateTimeField() # DatKont

    zav_a = models.IntegerField() # ZavA
    zav_b = models.IntegerField() # ZavB
    zav_c = models.IntegerField() # ZavC

    inspection_result = models.CharField(max_length=255, choices=InspectionResult.CHOICES, db_index=True) # VyslSTK
    emission_result = models.CharField(max_length=255, db_index=True, choices=EmissionResult.CHOICES) # VyslEmise

    vehicle = models.ForeignKey('stk.Vehicle', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.vehicle.vehicle_vendor} - {self.inspection_type}'


class Station(models.Model):
    stk_id = models.IntegerField(db_index=True, unique=True)
    authorization = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    tel_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)

    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        indexes = [
            HashIndex(fields=('region',))
        ]

    def __str__(self):
        return f'{self.stk_id} - {self.operator} - {self.city}'


class PrecalculatedStatistic(models.Model):
    region = models.CharField(max_length=255, blank=True, null=True)
    number_of_stations = models.IntegerField(default=0)
    number_of_inspections = models.IntegerField(default=0)

    eligible = models.IntegerField(default=0)
    ineligible = models.IntegerField(default=0)
    partially_eligible = models.IntegerField(default=0)
    # TODO: supported vehicles


class InspectionTypeStatistic(models.Model):
    precalculated_statistic = models.ForeignKey('stk.PrecalculatedStatistic', on_delete=models.CASCADE)
    inspection_type = models.CharField(max_length=255, choices=InspectionTypeNormalized.CHOICES, db_index=True) # DrTP
    repeated = models.BooleanField(default=False)
    number_of_inspections = models.IntegerField(default=0)

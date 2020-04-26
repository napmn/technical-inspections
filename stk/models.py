from django.db import models


# farby mapy nechat na uzivatelovi podla toho co chce

class Vehicle(models.Model):
    vehicle_vendor = models.CharField(max_length=255) # TZn
    vehicle_model = models.CharField(max_length=255) # ObchOznTyp 
    vehicle_type = models.CharField(max_length=255) # DrVoz
    vehicle_category = models.CharField(max_length=255) # Ct

    engine_type = models.CharField(max_length=255) # TypMot
    vin = models.CharField(max_length=255) # VIN
    km = models.IntegerField() # Km

    first_registration_date = models.DateField(null=True, blank=True) # DatPrvReg


class STKInspection(models.Model):
    stk_id = models.IntegerField() # STK
    inspection_type = models.CharField(max_length=255) # DrTP
    inspection_time = models.DateTimeField() # DatKont

    zav_a = models.IntegerField() # ZavA
    zav_b = models.IntegerField() # ZavB
    zav_c = models.IntegerField() # ZavC

    inspection_result = models.CharField(max_length=255) # VyslSTK
    emission_result = models.CharField(max_length=255) # VyslEmise

    vehicle = models.ForeignKey('stk.Vehicle', null=False, blank=False, on_delete=models.CASCADE)

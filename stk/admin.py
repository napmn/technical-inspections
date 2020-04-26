from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from stk.models import Vehicle, STKInspection

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_vendor', 'vehicle_model', 'vehicle_type', 'vehicle_category', 'km', 'first_registration_date'
    )

@admin.register(STKInspection)
class STKInspectionAdmin(admin.ModelAdmin):
    list_display = (
        'stk_id', 'inspection_type', 'inspection_time', 'zav_a', 'zav_b', 'zav_c', 'inspection_result',
        'emission_result', 'get_vehicle'
    )

    def get_vehicle(self, obj):
        return mark_safe(
            '<a href="{}" target="_blank">{}</a>'.format(
                reverse('admin:stk_vehicle_change', kwargs={'object_id': obj.vehicle.pk}), obj.vehicle.pk
            )
        )
    get_vehicle.short_description = 'Vehicle'

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from django_reverse_admin import ReverseModelAdmin

from stk.models import Vehicle, STKInspection, Station, PrecalculatedStatistic, InspectionTypeStatistic

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vehicle_vendor', 'vehicle_model', 'vehicle_type', 'vehicle_category', 'km',
        'first_registration_date'
    )


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('stk_id', 'city', 'address', 'operator', 'latitude', 'longitude', 'region')


class StationInlineAdmin(admin.StackedInline):
    model = Station


@admin.register(STKInspection)
class STKInspectionAdmin(ReverseModelAdmin):
    list_display = (
        'inspection_type', 'inspection_time', 'zav_a', 'zav_b', 'zav_c', 'inspection_result',
        'emission_result', 'get_vehicle'
    )
    inline_type = 'stacked'
    inline_reverse = [
        'station', 'vehicle'
    ]

    def get_vehicle(self, obj):
        return mark_safe(
            '<a href="{}" target="_blank">{}</a>'.format(
                reverse('admin:stk_vehicle_change', kwargs={'object_id': obj.vehicle.pk}), obj.vehicle.pk
            )
        )
    get_vehicle.short_description = 'Vehicle'


class InspectionTypeStatisticInline(admin.TabularInline):
    model = InspectionTypeStatistic


@admin.register(PrecalculatedStatistic)
class PrecalculatedStatisticAdmin(admin.ModelAdmin):
    list_display = (
        'region', 'number_of_stations', 'number_of_inspections', 'eligible', 'ineligible', 'partially_eligible'
    )
    inlines = [
        InspectionTypeStatisticInline
    ]

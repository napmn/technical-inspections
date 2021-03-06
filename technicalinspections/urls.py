from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from stk.api import PrecalculatedStatisticViewset, StatisticViewSet, StationsViewSet, VehicleVendorModelSuggestions


router = routers.DefaultRouter()
router.register(r'precalculated-stats', PrecalculatedStatisticViewset, basename='precalculated-stats')
router.register(r'stations', StationsViewSet, basename='stations')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats', StatisticViewSet.as_view({'get': 'get'}), name='stats'),
    path('vehicle-suggestions', VehicleVendorModelSuggestions.as_view({'get': 'get'}), name='vehicle-suggestions'),
    path('', include(router.urls))
]

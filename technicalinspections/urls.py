from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from stk.api import PrecalculatedStatisticViewset, StatisticViewSet


router = routers.DefaultRouter()
router.register(r'precalculated-stats', PrecalculatedStatisticViewset, basename='precalculated-stats')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stats', StatisticViewSet.as_view({'get': 'get'}), name='stats'),
    path('', include(router.urls))
]

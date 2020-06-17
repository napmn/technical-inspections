import logging

from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from stk.models import PrecalculatedStatistic, STKInspection, Station, Vehicle, VehicleName
from stk.serializers import PrecalculatedStatisticSerializer, StationSerializer, VehicleSuggestionSerializer


logger = logging.getLogger(__name__)


class PrecalculatedStatisticViewset(viewsets.ModelViewSet):
    serializer_class = PrecalculatedStatisticSerializer
    queryset = PrecalculatedStatistic.objects.all()
    filterset_fields = ['region']


class StatisticViewSet(viewsets.GenericViewSet):
    def get_queryset(self):
        return STKInspection.objects.all()

    def get(self, request):
        if not all(param in request.query_params for param in ('vehicle', 'region')):
            raise Http404('Mandatory query parameters are missing')

        vehicle = request.query_params['vehicle']
        region = request.query_params['region']
        stations = Station.objects.filter(region=region)
        vehicles = Vehicle.objects.filter(vehicle_vendor_model=vehicle)
        count = self.get_queryset().filter(station__in=stations, vehicle__in=vehicles).count()

        return Response({'count': count}, status=status.HTTP_200_OK)


class StationsViewSet(viewsets.ModelViewSet):
    serializer_class = StationSerializer
    lookup_field = 'stk_id'
    queryset = Station.objects.exclude(longitude=None)
    filterset_fields = ['region']


class VehicleVendorModelSuggestions(viewsets.ViewSet):
    def get(self, request):
        search = request.query_params.get('search', '')
        if len(search) < 3:
            suggestions = []
        else:
            vehicle_names = VehicleName.objects.filter(vendor_model__icontains=search)[:20]
            suggestions = VehicleSuggestionSerializer(vehicle_names, many=True).data

        return Response(suggestions, status=status.HTTP_200_OK)

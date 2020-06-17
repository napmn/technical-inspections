from rest_framework import serializers

from stk.models import PrecalculatedStatistic, InspectionTypeStatistic, Station, InspectionsInMonth


class InspectionTypeStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionTypeStatistic
        fields = ('inspection_type', 'repeated', 'number_of_inspections')


class InspectionsInMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionsInMonth
        fields = ('month', 'passed', 'not_passed')


class PrecalculatedStatisticSerializer(serializers.ModelSerializer):
    inspectiontypestatistic_set = InspectionTypeStatisticSerializer(many=True)
    inspectionsinmonth_set = InspectionsInMonthSerializer(many=True)

    class Meta:
        model = PrecalculatedStatistic
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class VehicleSuggestionSerializer(serializers.Serializer):
    name = serializers.CharField(source='vendor_model')

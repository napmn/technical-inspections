from rest_framework import serializers

from stk.models import PrecalculatedStatistic, InspectionTypeStatistic


class InspectionTypeStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionTypeStatistic
        fields = ('inspection_type', 'repeated', 'number_of_inspections')


class PrecalculatedStatisticSerializer(serializers.ModelSerializer):
    inspectiontypestatistic_set = InspectionTypeStatisticSerializer(many=True)

    class Meta:
        model = PrecalculatedStatistic
        fields = '__all__'


class DummySerializer(serializers.Serializer):
    count = serializers.IntegerField()

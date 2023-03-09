from rest_framework import serializers
from show.models import Temperature, co2

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['captime', 'captemperature']

class Co2Serializer(serializers.ModelSerializer):
    class Meta:
        model = co2
        fields = ['captime', 'capco2']
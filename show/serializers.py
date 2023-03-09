from rest_framework import serializers
from show.models import Temperature
class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['captime', 'captemperature']
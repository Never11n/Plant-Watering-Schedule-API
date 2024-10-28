from rest_framework import serializers

from plant_API.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
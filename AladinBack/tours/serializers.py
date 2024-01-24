from rest_framework import serializers
from .models import Tours, ComesOut, Days


class ToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'


class ComesOutStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComesOut
        fields = '__all__'


class DaysStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = '__all__'

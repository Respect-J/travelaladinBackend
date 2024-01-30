from rest_framework import serializers
from .models import Country, StepbyStep


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StepbyStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepbyStep
        fields = '__all__'


from rest_framework import serializers
from .models import Country, StepbyStep, Excluded, Contact


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StepbyStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepbyStep
        fields = '__all__'


class ExcludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excluded
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

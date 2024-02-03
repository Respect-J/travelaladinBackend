from rest_framework import serializers
from .models import Tours, ComesOut, Days, DateTours, ToursImg, PriceFor


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


class DateToursSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTours
        fields = '__all__'


class ToursImgSerializers(serializers.ModelSerializer):

    class Meta:
        model = ToursImg
        fields = '__all__'


class PriceForSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceFor
        fields = '__all__'

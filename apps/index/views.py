from rest_framework import generics
from .models import Country, StepbyStep, Excluded
from .serializers import CountrySerializer, StepbyStepSerializer, ExcludedSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StepbyStepListView(generics.ListAPIView):
    queryset = StepbyStep.objects.all()
    serializer_class = StepbyStepSerializer
# Create your views here.


class ExcludedListView(generics.ListAPIView):
    queryset = Excluded.objects.all()
    serializer_class = ExcludedSerializer
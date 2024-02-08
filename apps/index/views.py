from rest_framework import generics
from .models import Country, StepbyStep, Excluded, Contact
from .serializers import CountrySerializer, StepbyStepSerializer, ExcludedSerializer, ContactSerializer


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


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
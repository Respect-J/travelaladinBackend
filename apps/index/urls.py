from django.urls import path
from .views import CountryListView, StepbyStepListView, ExcludedListView
urlpatterns = [
    path('countre/', CountryListView.as_view(), name='CountryListView'),
    path('step/', StepbyStepListView.as_view(), name='StepbyStepListView'),
    path('step/', ExcludedListView.as_view(), name='ExcludedListView'),
]

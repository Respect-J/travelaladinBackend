from django.urls import path
from .views import CountryListView, StepbyStepListView, ExcludedListView, ContactListView
urlpatterns = [
    path('countre/', CountryListView.as_view(), name='CountryListView'),
    path('step/', StepbyStepListView.as_view(), name='StepbyStepListView'),
    path('excluded/', ExcludedListView.as_view(), name='ExcludedListView'),
    path('contact/', ContactListView.as_view(), name='ContactListView')
]

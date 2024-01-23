from django.urls import path
from .views import CountryListView, StepbyStepListView
urlpatterns = [
    path('countre/', CountryListView.as_view(), name='subjects-list-create'),
    path('step/', StepbyStepListView.as_view(), name='subjects-list-create'),
]

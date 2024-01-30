from django.urls import path
from .views import ToursListView, DaysStepListView, ComesOutStepListView, TourDetailView

urlpatterns = [
    path('', ToursListView.as_view(), name='subjects-list-create'),
    path('api/tour/<int:tour_id>/', TourDetailView.as_view(), name='tour-detail'),
]

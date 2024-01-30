from django.urls import path
from .views import ToursListView, DaysStepListView, ComesOutStepListView, TourDetailView, DateListView

urlpatterns = [
    path('', ToursListView.as_view(), name='subjects-list-create'),
    path('api/tour/<int:tour_id>/', TourDetailView.as_view(), name='tour-detail'),
    path('date/', DateListView.as_view(), name='Date-list-create')
]

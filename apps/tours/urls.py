from django.urls import path
from .views import ToursListView, TourPicsView, TourDetailView, DateListView, PriceListView, DateAListView

urlpatterns = [
    path('', ToursListView.as_view(), name='subjects-list-create'),
    path('api/tour/<int:tour_id>/', TourDetailView.as_view(), name='tour-detail'),
    path('date/', DateListView.as_view(), name='Date-list-create'),
    path('pics/<int:tour_id>/', TourPicsView.as_view(), name='get_photos_by_uuid'),
    path('price/', PriceListView.as_view(), name='Date-list-create'),
    path('dateautm/', DateAListView.as_view(), name='Date-list-create')
]

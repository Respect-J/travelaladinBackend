from rest_framework import generics
from .models import Tours, ComesOut, Days
from .serializers import ToursSerializer, ComesOutStepSerializer, DaysStepSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ToursListView(generics.ListAPIView):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer


class ComesOutStepListView(generics.ListAPIView):
    queryset = ComesOut.objects.all()
    serializer_class = ComesOutStepSerializer


class DaysStepListView(generics.ListAPIView):
    queryset = Days.objects.all()
    serializer_class = DaysStepSerializer
# Create your views here.



class TourDetailView(APIView):
    def get(self, request, tour_id, format=None):
        try:
            tour = Tours.objects.get(id=tour_id)
        except Tours.DoesNotExist:
            return Response({"error": "Tour not found"}, status=status.HTTP_404_NOT_FOUND)

        days_info = Days.objects.filter(tour=tour)
        comes_out_info = ComesOut.objects.filter(tour=tour)

        tour_serializer = ToursSerializer(tour)
        days_serializer = DaysStepSerializer(days_info, many=True)
        comes_out_serializer = ComesOutStepSerializer(comes_out_info, many=True)

        data = {
            'tour': tour_serializer.data,
            'days': days_serializer.data,
            'comes_out': comes_out_serializer.data
        }

        return Response(data)
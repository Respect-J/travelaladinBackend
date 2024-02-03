from rest_framework import generics
from .models import Tours, ComesOut, Days, DateTours, ToursImg, PriceFor, DateAUTUMNTours
from .serializers import ToursSerializer, ComesOutStepSerializer, DaysStepSerializer, DateToursSerializer, \
    ToursImgSerializers, PriceForSerializer, DateAUTUMNToursSerializer
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


class DateListView(generics.ListAPIView):
    queryset = DateTours.objects.all()
    serializer_class = DateToursSerializer


class DateAListView(generics.ListAPIView):
    queryset = DateAUTUMNTours.objects.all()
    serializer_class = DateAUTUMNToursSerializer


class PriceListView(generics.ListAPIView):
    queryset = PriceFor.objects.all()
    serializer_class = PriceForSerializer


class TourPicsView(APIView):
    def get(self, request, tour_id, format=None):
        try:
            tour = Tours.objects.get(id=tour_id)
        except Tours.DoesNotExist:
            return Response({"error": "Tour not found"}, status=status.HTTP_404_NOT_FOUND)

        pics_info = ToursImg.objects.filter(tour=tour)
        tour_serializer = ToursSerializer(tour)
        pics_serializer = ToursImgSerializers(pics_info, many=True)

        data = {
            'tour_info': tour_serializer.data,
            'pics_info': pics_serializer.data,
        }

        return Response(data)
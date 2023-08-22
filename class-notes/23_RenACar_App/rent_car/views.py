from django.shortcuts import render
from .serializers import CarSerializer, ReservationSerializer
from .models import Car, Reservation
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import date
from django.db.models import Q

# Create your views here.
class CarView(ListCreateAPIView):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    # permission_classes=[IsAdminUser]


class AvailableCarsView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not (start_date and end_date):
            return Response({"message": "start_date and end_date parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = date.fromisoformat(start_date)
            end_date = date.fromisoformat(end_date)
        except ValueError:
            return Response({"message": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        if start_date < date.today() or end_date < date.today():
            return Response({"message": "Past dates are not allowed."}, status=status.HTTP_400_BAD_REQUEST)

        if start_date > end_date:
            return Response({"message": "Start date cannot be after end date."}, status=status.HTTP_400_BAD_REQUEST)

        # Query available cars for the selected dates
        available_cars = Car.objects.filter(
            Q(reservation__start_date__gt=end_date) | Q(reservation__end_date__lt=start_date) | Q(reservation__isnull=True)
        )

        serializer = CarSerializer(available_cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationView(ListCreateAPIView):
    serializer_class=ReservationSerializer
    queryset=Reservation.objects.all()
    # permission_classes=[IsAdminUser]


from rest_framework.generics import RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]  # Sadece oturum açmış kullanıcılara izin verir.

class ReservationDeleteView(DestroyAPIView):
    queryset = Reservation.objects.all()
    permission_classes = [IsAuthenticated]  # Sadece oturum açmış kullanıcılara izin verir.

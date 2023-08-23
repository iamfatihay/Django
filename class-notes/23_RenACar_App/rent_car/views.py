from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Car, Reservation
from .serializers import CarSerializer, ReservationSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers


class CarListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['rent_per_day', 'brand']
    search_fields = ['plate_number', 'brand', 'model']

class ReservationListView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['start_date', 'end_date']
    search_fields = ['car__plate_number', 'customer__username']

    # def get_queryset(self):
    #     user = self.request.user
    #     user_id = self.request.user.id
    #     if user.is_superuser:
    #         return Reservation.objects.all()
    #     return Reservation.objects.filter(customer=user_id)


    # def get_queryset(self):
    #     # Oturum açmış kullanıcının kimliğini alın
    #     user_id = self.request.user.id

    #     # Kullanıcının rezervasyonlarını getirin
    #     queryset = Reservation.objects.filter(customer=user_id)
    #     return queryset

class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_update(self, serializer):
        user = self.request.user
        if serializer.instance.customer == user:
            serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        print("User ID:", user.id)
        print("Reservation Customer ID:", instance.customer.id)
    
        if instance.customer == user:
            instance.delete()
        else:
            print("User and Customer not matching.")
            return Response({"message": "You don't have permission to delete this reservation."}, status=status.HTTP_403_FORBIDDEN)
    
    def perform_create(self, serializer):
        car_id = serializer.validated_data['car_id']
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        # Kontrol edin: Bu araba belirtilen tarihlerde zaten kiralanmış mı?
        conflicting_reservations = Reservation.objects.filter(
            car_id=car_id,
            start_date__lte=end_date,
            end_date__gte=start_date
        )

        if self.request.user.is_authenticated:
            if conflicting_reservations.exists():
                raise serializers.ValidationError("This car is already reserved for the selected dates.")
            
            serializer.save(customer=self.request.user)
        else:
            return Response({"message": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)







###########






# from django.shortcuts import render
# from .serializers import CarSerializer, ReservationSerializer
# from .models import Car, Reservation
# from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAdminUser
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from datetime import date
# from django.db.models import Q

# # Create your views here.
# class CarView(ListCreateAPIView):
#     serializer_class=CarSerializer
#     queryset=Car.objects.all()
#     # permission_classes=[IsAdminUser]


# class AvailableCarsView(APIView):
#     def get(self, request):
#         start_date = request.query_params.get('start_date')
#         end_date = request.query_params.get('end_date')

#         if not (start_date and end_date):
#             return Response({"message": "start_date and end_date parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             start_date = date.fromisoformat(start_date)
#             end_date = date.fromisoformat(end_date)
#         except ValueError:
#             return Response({"message": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

#         if start_date < date.today() or end_date < date.today():
#             return Response({"message": "Past dates are not allowed."}, status=status.HTTP_400_BAD_REQUEST)

#         if start_date > end_date:
#             return Response({"message": "Start date cannot be after end date."}, status=status.HTTP_400_BAD_REQUEST)

#         # Query available cars for the selected dates
#         available_cars = Car.objects.filter(
#             Q(reservation__start_date__gt=end_date) | Q(reservation__end_date__lt=start_date) | Q(reservation__isnull=True)
#         )

#         serializer = CarSerializer(available_cars, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class ReservationView(ListCreateAPIView):
#     serializer_class=ReservationSerializer
#     queryset=Reservation.objects.all()
#     # permission_classes=[IsAdminUser]


# from rest_framework.generics import RetrieveUpdateDestroyAPIView, DestroyAPIView
# from rest_framework.permissions import IsAuthenticated

# class ReservationDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = ReservationSerializer
#     queryset = Reservation.objects.all()
#     permission_classes = [IsAuthenticated]  # Sadece oturum açmış kullanıcılara izin verir.

# class ReservationDeleteView(DestroyAPIView):
#     queryset = Reservation.objects.all()
#     permission_classes = [IsAuthenticated]  # Sadece oturum açmış kullanıcılara izin verir.
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer, ReservationSerializer
from .models import Car, Reservation
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrReadOnly

# Create your views here.
class CarView(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        # queryset = super().get_queryset()   #! 23.satirda "self." yazmassak bu satiri eklemeliyiz!
        
        
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if start and end:
            not_available=Reservation.objects.filter(end_date__gt=start,start_date__lt=end).values_list('id',flat=True)
            #! flat true id leri [1,3,7] listeye çeviriyor
            queryset = self.queryset.exclude(id__in=not_available).filter(availability=True)

        return queryset
    


class ReservationView(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
from rest_framework import serializers
from .models import Car, Reservation

class CarSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Car
        fields="__all__"

class ReservationSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Reservation
    #     fields = '__all__'

    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField(required=False)

    customer=serializers.StringRelatedField()
    customer_id=serializers.IntegerField(required=False)

    class Meta:
        model=Reservation
        fields=(
            "id",
            "car", 
            "car_id", 
            "customer",  
            "customer_id",
            )


from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields="__all__"
        fields = (
            "plate_number",
            "brand",
            "model",
            "year",
            "gear",
            "rent_per_day",
            "availability",
        )


class ReservationSerializer(serializers.ModelSerializer):
    # car = serializers.StringRelatedField()
    # car_id = serializers.IntegerField(required=False)
    # customer=serializers.StringRelatedField()
    # customer_id=serializers.IntegerField(required=False)
    class Meta:
        model=Reservation
        # fields = '__all__'
        fields = (
            "customer",
            "car",
            "start_date",
            "end_date",
        )
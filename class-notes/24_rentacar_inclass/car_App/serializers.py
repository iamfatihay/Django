from rest_framework import serializers
from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    is_available = serializers.BooleanField()
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
            'is_available',
        )
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request.user and not request.user.is_staff:
            fields.pop("plate_number")
            fields.pop("rent_per_day")
            fields.pop("availability") 
        return fields


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
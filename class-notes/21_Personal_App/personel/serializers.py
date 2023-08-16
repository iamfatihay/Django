from rest_framework import serializers
from .models import Department, Personel,Profile



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"   #! Gelmesini istediklerimizi yaziyoruz buraya
        exclude = []  #! Getirilmesini istemedigimiz field lari buraya yaziyoruz


class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = "__all__"   
        exclude = []

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"   
        exclude = []
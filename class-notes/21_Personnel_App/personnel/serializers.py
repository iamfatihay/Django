from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department, Personnel

#* her serializers da kullanilan ortak degerleri kendimiz ortak kullanilacak bir serializer olusturabiliriz.
class FixModel(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required = False)


class DepartmentSerializer(FixModel):
    # user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField(required = False)
    
    #! method field lar sadece read_only dir.
    personnel_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = "__all__" 
    
    def get_personnel_count(self,obj):
        return obj.personnels.count()


class PersonnelSerializer(FixModel):
    # user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField(required = False)

    class Meta:
        model = Personnel
        fields = "__all__"
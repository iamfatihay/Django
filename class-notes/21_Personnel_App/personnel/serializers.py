from rest_framework import serializers
from django.contrib.auth.models import User
from models. import Department, Personnel


class DepartmentSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField(required = False)

    class Meta:
        model = Department
        fields = "__all__" 

class PersonnelSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField(required = False)

    class Meta:
        model = Personnel
        fields = "__all__"
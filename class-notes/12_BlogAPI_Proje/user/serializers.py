from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
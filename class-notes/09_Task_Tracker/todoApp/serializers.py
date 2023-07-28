from rest_framework import serializers
from .models import Todo
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=(        #! (__all__) butun field lerin gelmesini istersek.
            'task',
            'description',
            'priority',
            'is_done',
            'created_date'
        )
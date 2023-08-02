from rest_framework import serializers
from .models import Blog, Category


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=("__all__")
        # fields=(  
        #     'id',      #! (__all__) butun field lerin gelmesini istersek.
        #     'task',
        #     'description',
        #     'priority',
        #     'is_done',
        #     'created_date'
        # )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
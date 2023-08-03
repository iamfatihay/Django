from rest_framework import serializers
from .models import Blog, Category


class BlogSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()  #! Models de olmak zorunda ve iliskili olmak zorunda
    user_id = serializers.IntegerField()   #! Veri tabaninda karsiligi olmak zorunda 

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model=Blog
        fields=("__all__")  #! (__all__) butun field lerin gelmesini istersek.
        # fields=(  
        #     'id',      
        #     'task',
        #     'description',
        #     'priority',
        #     'is_done',
        #     'created_date'
        # )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"   #! Gelmesini istediklerimizi yaziyoruz buraya
        exclude = []  #! Getirilmesini istemedigimiz field lari buraya yaziyoruz
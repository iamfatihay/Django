"""Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes
 that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization,
   allowing parsed data to be converted back into complex types, after first validating the incoming data.  """

from rest_framework import serializers
from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
#     age = serializers.IntegerField()


#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):

    born_year = serializers.SerializerMethodField()  #read_only
    #! read_only, post isleminde devreye girmeyip get islemi esnasinda dahil oluyor. "MethodField" nin bir ozelligi bu,
    #! ve tablomuzda bu field gpzukmeyecek.
    path = serializers.StringRelatedField() # read_only
    #* "StringRelatedField" foreign key oldugunda ilgili id nosunu verdigi icin, bu kod ile ilgili string donuyor.
    path_id = serializers.IntegerField()


    class Meta:
        model = Student
        fields = "__all__"
        # fields = ("first_name", "age")

    def get_born_year(self,obj): 
        #! methodField buraya atanacak degeri icin fonk. get ile baslamasi gerekiyor, ve ustteki variable nin ismini almasi gerekiyor 
        import datetime
        current_time = datetime.datetime.now()
        return current_time.year - obj.age    
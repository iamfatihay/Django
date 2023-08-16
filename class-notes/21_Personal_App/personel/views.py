from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer, PersonelSerializer,ProfileSerializer
from .models import Department, Personel, Profile


class Department(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

class Personel(ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer

class Profile(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
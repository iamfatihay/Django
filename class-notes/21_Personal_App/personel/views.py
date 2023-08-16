from rest_framework.viewsets import ModelViewSet
from .serializers import DepartmentSerializer, PersonelSerializer
from .models import Department, Personel


class Department(ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

class Personel(ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
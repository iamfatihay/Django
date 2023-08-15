from .serializers import TutorialSerializer
from .models import Tutorial
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TutorialMVS(ModelViewSet):
    queryset= Tutorial.objects.all()
    serializer_class= TutorialSerializer
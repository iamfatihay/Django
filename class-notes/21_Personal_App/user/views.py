from rest_framework.viewsets import ModelViewSet
from .serializers import (
    User, UserSerializer
)

from rest_framework.permissions import IsAdminUser
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


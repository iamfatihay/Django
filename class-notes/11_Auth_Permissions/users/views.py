# from rest_framework.generics import CreateAPIView
# from django.contrib.auth.models import User
# from .serializers import RegisterSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view


# class RegisterView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#         token = Token.objects.create(user_id=user.id)
#         data = serializer.data
#         data["token"] = token.key
#         headers = self.get_success_headers(serializer.data)
#         return Response(
#             data, status=status.HTTP_201_CREATED, headers=headers
#         )

#     def perform_create(self, serializer):
#         user=serializer.save()
#         return user


from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = Token.objects.create(user_id=user.id)
        data = serializer.data
        data["token"] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        return user


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(user_id=response.data["user_id"])
        response.data["token"] = token.key
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_authenticated:
            # Token geçerliliğini sonlandır ve silelim
            request.user.auth_token.delete()
            # Kullanıcının oturumunu kapatmak için Django'dan logout çağrısı yapalım
            logout(request)
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "User is not authenticated"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

from django.urls import path

# from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserView

# ------------------------------------------------
# Login:
from rest_framework.authtoken.views import obtain_auth_token
# ------------------------------------------------
# Logout:
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def logout(request):
    # print(dir(request.user))  #! request in icinde ne gelioyr gormek icin
    request.user.auth_token.delete() # Token Sil.
    return Response({"message": 'User Logout: Token Deleted'})
# ------------------------------------------------
# Login/Logout
urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', logout),
]
# ------------------------------------------------

# ROUTER:
router = DefaultRouter()
router.register('', UserView)

urlpatterns += router.urls
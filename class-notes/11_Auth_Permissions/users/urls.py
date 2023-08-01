from django.urls import path, include
# from .views import RegisterView, logout_view
from .views import RegisterView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', RegisterView.as_view()),  #! Class based view kullanirken "as_view" sart
    path('login', obtain_auth_token),
    # path('logout', logout_view),
    path('logout', LogoutView.as_view()),

]

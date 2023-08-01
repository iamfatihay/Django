
from django.urls import path, include
from .views import RegisterView


urlpatterns = [
    path('register', RegisterView.as_view()),  #! Class based view kullanirken "as_view" sart

]

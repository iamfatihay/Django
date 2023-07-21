from django.urls import path
from .views import dswelcome

# from fsApp.views import fswelcome
# from dsApp.views import dswelcome


urlpatterns = [
    path('', dswelcome),
]
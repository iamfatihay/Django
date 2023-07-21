from django.urls import path
from .views import fswelcome

# from fsApp.views import fswelcome
# from dsApp.views import dswelcome


urlpatterns = [
    path('', fswelcome),
]
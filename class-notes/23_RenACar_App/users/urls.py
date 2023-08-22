from django.urls import path,include
from .views import RegisterView,ProfileUpdateView

urlpatterns = [
    #login, logout
    path('auth/', include('dj_rest_auth.urls')),
    #register
    path('register/',RegisterView.as_view()),
    path('profile/<int:pk>',ProfileUpdateView.as_view()),

    
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarView, ReservationView, ReservationRUDView

router = DefaultRouter()
router.register("car", CarView)

urlpatterns = [
    path('reservation/', ReservationView.as_view()),
    path('reservation/<int:pk>', ReservationRUDView.as_view()),
]
urlpatterns += router.urls
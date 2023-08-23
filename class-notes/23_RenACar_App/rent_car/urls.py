from django.urls import path
from .views import CarListView, ReservationListView, ReservationDetailView

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
]
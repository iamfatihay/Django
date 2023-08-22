from django.urls import path
from .views import AvailableCarsView, ReservationView, ReservationDetailView, ReservationDeleteView

urlpatterns = [
    path('cars/', AvailableCarsView.as_view(), name='available-cars'),
    path('reservations/', ReservationView.as_view(), name='reservations'), 
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'),
]

from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from .views import FlightView

#! class isminin sonu "TestCase" olmali

class FlightTestCase(APITestCase):
    def setUp(self):
        self.factory=APIRequestFactory

    #! fonksiyon yazarken de "test" ile baslamali isim
    def test_flight_list(self):
        request=self.factory.get("/flights")
        response=
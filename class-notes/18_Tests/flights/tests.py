from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status
from .views import FlightView
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.authtoken.models import Token
from .models import Flight

#! class isminin sonu "TestCase" olmali


class FlightTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username="fatih",
            email="f@gmail.com",
            password="secret11",
        )

        self.token = Token.objects.get(user=self.user)
        # To update a flight, we need to have one. 
        self.flight = Flight.objects.create( 
            id=1, 
            flight_number="AA100", 
            operation_airlines="AHY", 
            departure_city="Antalya", 
            arrival_city="Amsterdam", 
            date_departure="2022-12-01", 
            estimated_time="15:00:00")

    #! fonksiyon yazarken de "test" ile baslamali isim
    def test_flight_list_as_guest(self):
        request = self.factory.get("/flights")
        response = FlightView.as_view({"get": "list"})(request)
        # request.user=AnonymousUser()
        self.assertEqual(response.status_code, 200)

    def test_flight_create_as_guest(self):
        request = self.factory.post("/flights")
        response = FlightView.as_view({"post": "create"})(request)
        request.user = AnonymousUser()
        self.assertEqual(response.status_code, 401)

    def test_flight_create_as_login(self):
        request = self.factory.post(
            "/flights", HTTP_AUTHORIZATION="Token " + self.token.key
        )
        response = FlightView.as_view({"post": "create"})(request)
        self.assertEqual(response.status_code, 403)

    def test_flight_create_as_admin(self):
        data = {
            "flight_number": "UK100",
            "operation_airlines": "UHY",
            "departure_city": "Untalya",
            "arrival_city": "Umsterdam",
            "date_departure": "2022-12-03",
            "estimated_time": "15:27:22",
        }
        request = self.factory.post('/flight/flights/', data, HTTP_AUTHORIZATION='Token {}'.format(self.token)) 
        # And make this user a staff, do not forget to save it 
        self.user.is_staff = True 
        self.user.save() 
        force_authenticate(request, user=self.user) 
        response = FlightView.as_view({'post': 'create'})(request) 
        self.assertEqual(response.status_code, 201) 
        # Another way to check everything is ok 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # def test_flight_create_as_admin(self):
        #     data = {
        #         "flight_number": "TK100",
        #         "operation_airlines": "THY",
        #         "departure_city": "Antalya",
        #         "arrival_city": "Amsterdam",
        #         "date_departure": "2022-12-03",
        #         "estimated_time": "15:27:22"
        #     }
        #     request = self.factory.post('/flights',data, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        #     self.user.is_staff=True
        #     self.user.save()
        #     force_authenticate(request, user=self.user)
        #     response=FlightView.as_view({'post': 'create'})(request)
        #     self.assertEqual(response.status_code,201)

    def test_flight_update_as_staff_user(self): 
        # Without sending data it gives 400 Bad Request 
        data = {
            "flight_number": "UK100",
            "operation_airlines": "UHY",
            "departure_city": "Antalya",
            "arrival_city": "Umsterdam",
            "date_departure": "2022-12-03",
            "estimated_time": "15:27:22",
        } 
        request = self.factory.put('/flight/flights/1/', data, HTTP_AUTHORIZATION='Token {}'.format(self.token)) 
        self.user.is_staff = True 
        self.user.save() 
        force_authenticate(request, user=self.user) 
        response = FlightView.as_view({'put': 'update'})(request, pk='1') 
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(Flight.objects.count(), 1) 
        self.assertEqual(Flight.objects.get().flight_number, 'UK100')

    def test_flight_str(self): 
        self.assertEqual(str(self.flight),f"{self.flight.flight_number} - {self.flight.departure_city}- {self.flight.arrival_city}")

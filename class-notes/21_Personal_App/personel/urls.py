from django.urls import path, include
from .views import Department, Personel, Profile
from rest_framework import routers

router=routers.DefaultRouter()
router.register("department", Department)
router.register('personel', Personel)
router.register('profile', Profile)

urlpatterns = router.urls
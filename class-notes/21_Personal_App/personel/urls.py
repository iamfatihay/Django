from django.urls import path, include
from .views import Department, Personel
from rest_framework import routers

router=routers.DefaultRouter()
router.register("department", Department)
router.register('personel', Personel)

urlpatterns = router.urls
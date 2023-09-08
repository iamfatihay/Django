from django.urls import path
from rest_framework import routers
from .views import (
    CategoryView,BrandView, ProductView
)


router = routers.DefaultRouter()
router.register("categories", CategoryView)
router.register("brands", BrandView)
router.register("products", ProductView)

urlpatterns = [
    #path('register/', RegisterView.as_view()),
]+router.urls

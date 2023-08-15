
from django.urls import path
from .views import TutorialMVS
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("tutorials",TutorialMVS)

urlpatterns = router.urls

#!fbv

# urlpatterns += [
#     path("tutorialsfbv/",tutorial_list,name="tutorial"),
#     path("tutorialsfbv/<int:id>",tutorial_detail,name="tutorial_detail"),
# ]
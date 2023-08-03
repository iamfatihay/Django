from rest_framework import routers
from .views import UserView

# ROUTER:
router=routers.DefaultRouter()
router.register('', UserView)


urlpatterns = router.urls
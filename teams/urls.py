from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet


router = routers.SimpleRouter()
router.register("", TeamViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

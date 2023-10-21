from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet


router = routers.SimpleRouter()
router.register("", PersonViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

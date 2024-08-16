from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r"networknodes", NetworkNodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

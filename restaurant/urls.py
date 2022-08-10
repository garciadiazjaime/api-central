from django.urls import path, include
from rest_framework import routers

from .views import index, UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

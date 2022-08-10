from django.http import HttpResponse
from rest_framework import viewsets

from restaurant.serializer import RestaurantSerializer
from restaurant.models import Restaurant


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

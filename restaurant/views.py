from rest_framework.generics import ListAPIView, RetrieveAPIView

from restaurant.serializer import RestaurantSerializer
from restaurant.models import Restaurant


class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetails(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'slug'
    

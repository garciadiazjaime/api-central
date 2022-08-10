from rest_framework import serializers

from .models import Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'instagram', 'image', 'description', 'category', 'location']

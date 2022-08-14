from rest_framework import serializers

from restaurant.models import Restaurant

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'slug',
            'instagram',
            'image',
            'description',
            'category',
            'phone',
            'address',
            'gmaps',
            'latitude',
            'longitude'
        ]
    
    phone = serializers.CharField(source='location.phone')
    address = serializers.CharField(source='location.address')
    gmaps = serializers.CharField(source='location.gmaps')
    latitude = serializers.CharField(source='location.latitude')
    longitude = serializers.CharField(source='location.longitude')

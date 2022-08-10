import json

from restaurant.models import Location, Restaurant

f = open("./scripts/restaurants.json")

data = json.load(f)

for place in data:
    location, _ = Location.objects.get_or_create(
        phone = place['phone'],
        address = place['address'],
        gmaps = place['gmaps'],
        latitude = place['latitude'],
        longitude = place['longitude']
    )
    
    Restaurant.objects.get_or_create(
        name = place['name'],
        instagram = place['instagram'],
        image = place['image'],
        description = place['description'],
        category = 'desayuno',
        location = location
    )


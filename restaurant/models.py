from django.db import models

class Location(models.Model):
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    gmaps = models.CharField(max_length=400)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant.name if hasattr(self, 'restaurant')  else str(self.id)


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    instagram = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return f"{self.name} - {self.slug}"


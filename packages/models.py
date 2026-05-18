from django.db import models
from cloudinary.models import CloudinaryField

class HeroSlider(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=250)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

class TourPackage(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    itinerary = models.TextField(null=True, blank=True)
    inclusions = models.TextField(null=True, blank=True)
    exclusions = models.TextField(null=True, blank=True)
    image = CloudinaryField('image')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='bookings')
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=20)
    travel_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.package.name} by {self.guest_name}"
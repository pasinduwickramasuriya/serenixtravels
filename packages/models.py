from django.db import models
from cloudinary.models import CloudinaryField

class HeroSlider(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=250)
    image = CloudinaryField('image', null=True, blank=True)
    image_link = models.URLField(max_length=1000, blank=True, null=True, help_text="Or paste a direct image URL link instead of uploading an image file")

    @property
    def image_url(self):
        if self.image_link:
            return self.image_link
        elif self.image:
            return self.image.url
        return ""

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
    image = CloudinaryField('image', null=True, blank=True)
    image_link = models.URLField(max_length=1000, blank=True, null=True, help_text="Or paste a direct image URL link instead of uploading an image file")
    is_featured = models.BooleanField(default=False)

    @property
    def image_url(self):
        if self.image_link:
            return self.image_link
        elif self.image:
            return self.image.url
        return ""

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('package_detail', args=[self.pk])

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
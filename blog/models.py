from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    caption = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.caption
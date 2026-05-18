from django.db import models
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    caption = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.caption
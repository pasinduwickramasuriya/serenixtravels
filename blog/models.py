from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)
    image_link = models.URLField(max_length=1000, blank=True, null=True, help_text="Or paste a direct image URL link instead of uploading an image file")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def image_url(self):
        if self.image_link:
            return self.image_link
        elif self.image:
            return self.image.url
        return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', args=[self.slug])

class GalleryImage(models.Model):
    caption = models.CharField(max_length=100)
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
        return self.caption
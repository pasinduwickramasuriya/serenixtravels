from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from packages.models import TourPackage
from blog.models import BlogPost

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'contact', 'package_list', 'blog_list']

    def location(self, item):
        return reverse(item)

class TourPackageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return TourPackage.objects.all()

class BlogPostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return BlogPost.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at

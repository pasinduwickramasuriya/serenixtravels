from django.shortcuts import render
from packages.models import HeroSlider, TourPackage
from blog.models import BlogPost, GalleryImage

def home(request):
    slides = HeroSlider.objects.all()
    packages = TourPackage.objects.all()[:6]
    recent_posts = BlogPost.objects.all().order_by('-created_at')[:3]
    gallery = GalleryImage.objects.all()[:8]
    
    return render(request, 'index.html', {
        'slides': slides,
        'featured_packages': packages,
        'recent_posts': recent_posts,
        'gallery': gallery
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
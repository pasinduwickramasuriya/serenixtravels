from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/list.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Blog

# Create your views here.

def blog(request):

    blog_post = Blog.objects.all().filter(is_published=True)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blogging/blog.html', context)


def blogsingle(request, id):
    blog_list = Blog.objects.all().filter(is_published=True)

    context = {
        'blog_list': blog_list,
    }

    return render(request, 'blogging/blogsingle.html', context)
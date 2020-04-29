from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment, Tag

# Create your views here.

def blog(request):

    blog_post = Blog.objects.all().filter(is_published=True)
    comments = Comment.objects.all()
    context = {
        'blog_post': blog_post,
        'comments': comments,
    }

    return render(request, 'blogging/blog.html', context)


#@login_required(login_url='login')
def blogsingle(request, id):
    blog_list = Blog.objects.all().filter(is_published=True)
    blog = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_on')
    

    context = {
        'blog_list': blog_list,
        'comments': comments,
    }

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        comment = Comment(name=name, email=email, message=message, blog=blog)
        comment.save()


    return render(request, 'blogging/blogsingle.html', context)


        
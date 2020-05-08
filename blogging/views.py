from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Blog, Comment, Tag

# Create your views here.

def blog(request):

    blog_post = Blog.objects.all().filter(is_published=True)
    comments = Comment.objects.all()


    paginator = Paginator(blog_post, 6)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blog_post': paged_blogs,
        'comments': comments,
    }

    return render(request, 'blogging/blog.html', context)


#@login_required(login_url='login')
def blogsingle(request, id):
    blog_list = Blog.objects.all().filter(is_published=True)
    blog = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_on')
    tags = Tag.objects.all()
    popular_articles = Blog.objects.annotate(num_comment=Count('comments')).order_by('-num_comment')[:3]
    print(popular_articles)

    

    context = {
        'popular': popular_articles,
        'tags': tags,
        'blog': blog,
        'blog_list': blog_list,
        'comments': comments,
    }

    #comments
    if request.method == 'POST':

        name = request.user.username
        email = request.user.email
        message = request.POST['message']
        
        comment = Comment(name=name, email=email, message=message, blog=blog)
        comment.save()


    return render(request, 'blogging/blogsingle.html', context)


def search(request):
    queryset_list = Blog.objects.all().filter(is_published=True)
    query = request.GET.get('keywords')
    if query:
        queryset_list = queryset_list.filter(
            Q(text1_bs__icontains=query)|
            Q(text2_bs__icontains=query)|
            Q(text3_bs__icontains=query)|
            Q(title__icontains=query)|
            Q(author__icontains=query)|
            Q(header1_bs__icontains=query)|
            Q(header2_bs__icontains=query)|
            Q(name_person_bs__icontains=query)|
            Q(text_person_bs__icontains=query)
        ).distinct()

    context = {
        'queryset_list': queryset_list,
    }    

    return render(request, 'pages/search_results.html', context)

    
    
    return redirect('menu')


def tag_search(request):
    query = Blog.objects.all().filter(is_published=True)
    return
        
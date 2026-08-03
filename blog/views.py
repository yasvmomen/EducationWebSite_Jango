
from django.shortcuts import render, get_object_or_404
from blog.models import post
# Create your views here.
app_name = 'blog'

def blog_view (request,author_username=None) :
    posts = post.objects.filter(status=1)
    if author_username :
        posts=posts.filter(auther__username=author_username)
    context = {'posts' : posts}
    return render (request, 'blog/blog-home.html', context)

def blog_single (request, pid) :
    #context = {'title' : 'how to conect database to your project', 'content' : 'this is a doc to learn', 'auther' : 'Y_vmn'}
    posts = get_object_or_404 (post, pk=pid, status=1)
    context = {'post' : posts}
    return render (request, 'blog/blog-single.html', context)

def ttest (request, pid) :
    #posts = post.objects.filter(status=1)
    #posts = post.objects.get(id=pid)
    posts = get_object_or_404 (post, pk=pid)
    context = {'post' : posts}
    return render (request, 'ttest.html', context)


def blog_search (request) :
    posts = post.objects.filter(status=1) 
    if request.method=='GET' :
        print(request.GET.get('s'))
        if s := request.GET.get('s') :
            posts = posts.filter(Content__contains=s)
       
    context = {'posts' : posts}
    return render (request, 'blog/blog-home.html', context)
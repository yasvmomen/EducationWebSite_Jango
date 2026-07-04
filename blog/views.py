
from django.shortcuts import render

# Create your views here.
app_name = 'blog'

def blog_view (request) :
    return render (request, 'blog/blog-home.html')

def blog_single (request) :
    context = {'title' : 'how to conect database to your project', 'content' : 'this is a doc to learn', 'auther' : 'Y_vmn'}
    return render (request, 'blog/blog-single.html', context)
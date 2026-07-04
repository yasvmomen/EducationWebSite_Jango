
from django.shortcuts import render

# Create your views here.
app_name = 'blog'

def blog_view (request) :
    return render (request, 'blog/blog-home.html')

def blog_single (request) :
    return render (request, 'blog/blog-single.html')
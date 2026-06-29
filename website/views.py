from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

#def http_test (request) :
#    return HttpResponse ('Hello world/django version')
#    return HttpResponse ('<h1>this is a test.</h1>')
 
#def json_test (request) :
#     return JsonResponse ({'Name' : 'YAS'})

def home_view (request) :
    #return HttpResponse ('<h1>Home Page ...</h1>')
    return render(request, 'website/index.html')

def about_view (request) :
    #return HttpResponse ('<h1>about Page ...</h1>')
    return render(request, 'website/about.html')



def contact_view (request) :
    #return HttpResponse ('<h1>contact Page ...</h1>')
    return render(request, 'website/contact.html')
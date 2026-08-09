from django.shortcuts import render
from website.models import contact
from website.forms import ContactForm
from django.contrib import messages

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
    if request.method == 'POST' :
        form =  ContactForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request,messages.SUCCESS,'پیغام شما با موفقیت ارسال شد')
        else :
            messages.add_message(request,messages.ERROR,'مشکلی رخ داده است، لطفا دوباره تلاش کنید')
    form = ContactForm()
    return render(request, 'website/contact.html',{'form':form})

def test_view (request) :
    return render(request, 'website/test.html', {'name' : 'ostad', 'famil' : 'farahi'})
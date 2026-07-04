
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    
    #path ('http/test',http_test),
    #path ('json-test', json_test)

    path ('home', home_view , name= 'index'),
    path ('', home_view , name= 'index'),
    path ('about', about_view , name= 'about'),
    path ('contact', contact_view , name= 'contact'),
    path ('test', test_view , name= 'test')
]
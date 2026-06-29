
from django.urls import path
from website.views import *

urlpatterns = [
    
    #path ('http/test',http_test),
    #path ('json-test', json_test)

    path ('home', home_view),
    path ('', home_view),
    path ('about', about_view),
    path ('contact', contact_view)
]
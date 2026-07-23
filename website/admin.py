from django.contrib import admin

# Register your models here.
from website.models import contact


class contactAdmin (admin.ModelAdmin) :
    date_hierarchy = 'created_date'
    list_filter = ('name', 'email', 'subject')
    search_fields = ('name', 'message', 'email', 'subject')
    list_display = ('name', 'email', 'subject','created_date','updated_date')
admin.site.register(contact, contactAdmin)
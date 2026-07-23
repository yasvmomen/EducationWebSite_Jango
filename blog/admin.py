from django.contrib import admin

# Register your models here.
from blog.models import post,category 

# also we can use decorates insted of this : admin.site.register(post, postAdmin) :
# we can usethis : @admin.register(post)
class postAdmin (admin.ModelAdmin) :
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('Title', 'auther', 'counted_views','published_date','status')
    list_filter = ('status',)
    #ordering = ['created_date'] #we can add it in models classes as Meta class
    search_fields = ['Title', 'Content']

admin.site.register(category)
admin.site.register(post, postAdmin)
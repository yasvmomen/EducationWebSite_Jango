from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.

class category (models.Model) :
    
    name = models.CharField(max_length=255)

    class Meta () :
        verbose_name = "کتگوری"
        verbose_name_plural = "کتگوری ها"

    def __str__(self):
        return self.name
    

class post (models.Model) :

    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Title = models.CharField (max_length=255)
    Content = models.TextField ()
    # tag
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField (default=0)
    status = models.BooleanField (default=False)
    published_date = models.DateTimeField (null=True)
    created_date = models.DateTimeField (auto_now_add=True)
    updated_date = models.DateField (auto_now=True)

    class Meta () :
        ordering = ['-created_date']
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__ (self) :
        return "{} - {}".format(self.Title,self.id)
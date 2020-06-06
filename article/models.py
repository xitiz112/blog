from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    ARTICLES_category=(('1',"politics"),('2',"sports"),('3',"entertainment"))
    title= models.CharField(max_length=200)
    content= models.TextField()
    image= models.ImageField(upload_to="uploads",null=True)
    author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    reported_at= models.CharField(max_length=30)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    category= models.CharField(max_length=2,choices=ARTICLES_category)


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
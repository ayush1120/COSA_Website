from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    



class Club(models.Model):

    name = models.CharField(max_length=25,primary_key=True,blank=False,null=False)
    
    description = models.TextField(max_length=None,blank=False,editable=True)

    members = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):  
        return self.name



class Batch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

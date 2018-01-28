from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usernotes(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    notes = models.CharField(max_length = 1000)
    subject = models.CharField(max_length = 300,default="Subject")




from django.db import models

# Create your models here.
#app name: contactUs
class contact_link(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    
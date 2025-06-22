from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount

#app name: UserProfile
# Create your models here.
def imgprofileSave(instance,filename):
    name,extention = filename.split('.')
    return "profile/imgicon/%s.%s"%(instance.id,extention)


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    total_paid = models.IntegerField(default=0)
    phone_number = models.CharField(default='',max_length=15)
    gender = models.CharField(default="Male",choices={("Male","Male"),("Female","Female")}, max_length=10)
    image = models.ImageField(upload_to=imgprofileSave,null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    

    
@receiver(post_save, sender=SocialAccount)
def _post_save_receiver(sender,instance,created, **kwargs):
    if created:
        profile.objects.create(user=instance.user,birth_date="2000-01-01",total_paid=0,phone_number="",gender="Male")
 



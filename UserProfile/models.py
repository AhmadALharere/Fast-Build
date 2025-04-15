from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#app name: UserProfile
# Create your models here.
def imgprofileSave(instance,filename):
    name,extention = filename.split('.')
    return "profile/imgicon/%s.%s"%(instance.id,extention)


class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    BMBC_coins = models.IntegerField()
    total_paied = models.IntegerField(default=0)
    
    #city
    phone_number = models.CharField(default='',max_length=15)
    image = models.ImageField(upload_to=imgprofileSave)
    #LikedParts
    
        
    def __str__(self):
        return self.user.username
    
    
    

    
@receiver(post_save, sender=User)
def _post_save_receiver(sender,instance,created, **kwargs):
    if created:
        profile.objects.create(user=instance,BMBC_coins=0)
 



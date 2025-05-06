from django.db import models
from django.contrib.auth.models import User
from PcPart.models import Part
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications",null=True,blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False) # حالة الاشعارات
    created_at = models.DateTimeField(auto_now_add=True)


class Like (models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    part = models.ForeignKey(Part ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ('user','part') # مشان يمنع الاعجاب اكثر من مرة
        
    def __str__(self):
        return f"{self.user.username} أعجب بـ {self.Part.name}" #يقوم بارجاع نص وصفي  


    
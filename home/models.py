from django.db import models
from django.contrib.auth.models import User
from PcPart.models import Part
from django.db.models.signals import post_save
from django.dispatch import receiver
from Cart.models import Cart,Discount
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications",null=True,blank=True)
    title = models.CharField(max_length=50,default="")
    message = models.TextField()
    is_read = models.BooleanField(default=False) # حالة الاشعارات
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(post_save,sender=Cart)
def _notify_cart_posted(sender,instance,created,**kwargs):
    if created:
        Notification.objects.create(
            user=instance.client,
            title = "your cart had posted successfuly!!",
            message= f"in date {instance.order_date} you ordered a cart with id : {instance.id} , now please wait for our team to make your order ready and stay alert for a further note for you.",
            is_read = False
        )

@receiver(post_save, sender=Cart)
def _notify_cart_status_change(sender, instance, created, **kwargs):
    if not created:
        try:
            old_instance = Cart.objects.get(pk=instance.pk)
        except Cart.DoesNotExist:
            return

        if old_instance.status != instance.status:
            messages = {
            "Waiting":f"your order with id: {instance.id} comeback successfuly to waiting line, please wait again until further notice...",
            "Ready":f"Congratulation!!!\n your cart now is ready in our centers, please go to take it and pay for it with {instance.total_cost}$",
            "Done":f"thank you for buying from owr app,and waiting for your visit again...",
            "Canceled":f"Cart status has been modified to : {instance.status}.",
            "Rejected":f"sorry but your cart rejected by our team, team message: {instance.team_message}"
            }
            Notification.objects.create(
                user=instance.client,
                title="Cart status modified!!",
                message=messages[instance.status],
                is_read=False
            )
            
@receiver(post_save,sender=User)
def _notify_user_welcome(sender,instance,created,**kwargs):
    if created:
        Notification.objects.create(user=instance
                                    ,title="Welcome Message!!"
                                    ,message="thank you for registering in our app, we wish for you to have a good time with us!!"
                                    ,is_read=False)
        
@receiver(post_save,sender=Part)
def _notify_part_posted(sender,instance,created,**kwargs):
    if created:
        Notification.objects.create(
            user=None,
            title = "New Part Has been added!!",
            message= f"New Part Has been added to our collections, you can now find the part: {instance.name} in {instance.content_type.model} category!",
            is_read = True
        )

@receiver(post_save,sender=Discount)
def _notify_discount_posted(sender,instance,created,**kwargs):
    if created:
        Notification.objects.create(
            user=None,
            title = "New offer Has been added!!",
            message= f"New Discount has been added to the part {instance.part.name} , you can now git it by just {instance.new_price}$ instead of {instance.part.price}$ start from {instance.start_date} to {instance.end_date}",
            is_read = True
        )




class Like (models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    part = models.ForeignKey(Part ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        unique_together = ('user','part') # مشان يمنع الاعجاب اكثر من مرة
        
    def __str__(self):
        return f"{self.user.username} put like on {self.Part.name}" #يقوم بارجاع نص وصفي  


    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#app name: home
state_list = (
    ("Waiting","Waiting"),
    ("Ready","Ready"),
    ("Done","Done"),
    ("Canceled","Canceled"),
    ("Rejected","Rejected")
    )



class Cart(models.Model):
    
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    total_cost = models.FloatField(default=0.0)
    status = models.CharField(default="Waiting",choices=state_list,max_length=10) 
    team_message = models.TextField(null=True,blank=True,default=None)

    def __str__(self):
        return f"Cart {self.id}"


class order(models.Model):
    
    basket = models.ForeignKey("Cart",related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey("PcPart.Part", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0.0)
    def __str__(self):
        return f"order in {self.basket}"
    
    


class Discount(models.Model):
    
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_valid = models.BooleanField()
    part = models.OneToOneField("PcPart.Part", on_delete=models.CASCADE)
    new_price = models.FloatField(default=0.0)
    

    def __str__(self):
        return f"discount on {self.part}"    
    

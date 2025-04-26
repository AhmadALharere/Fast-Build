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



class ShopBascet(models.Model):
    
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    total_cost = models.IntegerField(default=0)
    state = models.CharField(default="Waiting",choices=state_list,max_length=10) 
    

    def __str__(self):
        return f"bascet {self.id} on date: {self.order_date}"


class order(models.Model):
    
    bascet = models.ForeignKey("ShopBascet",related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey("PcPart.Part", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product
    
    


class Descount(models.Model):
    
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField()
    is_quantity_limit = models.BooleanField()
    is_dated_limit = models.BooleanField()
    part = models.ForeignKey("PcPart.Part", on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f"descount on {self.part}"    
    

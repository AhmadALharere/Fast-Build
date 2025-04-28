from django.contrib import admin
from .models import ShopBasket,order,Discount
# Register your models here.




from django.db.models import Exists, OuterRef


admin.site.register(ShopBasket)
admin.site.register(order)
admin.site.register(Discount)
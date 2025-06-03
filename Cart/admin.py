from django.contrib import admin
from .models import Cart,order,Discount
# Register your models here.




from django.db.models import Exists, OuterRef


admin.site.register(Cart)
admin.site.register(order)
admin.site.register(Discount)
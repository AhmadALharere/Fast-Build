from django.contrib import admin
from .models import BC_Collection,Collection_order,memory_unit,storage_unit,Gpu_unit,Case_Fan_unit,extra_storage_unit,accessory_unit,optical_drive_unit
# Register your models here.


class memory_unit_inline(admin.TabularInline):
    model = memory_unit
    extra = 1

class storage_unit_inline(admin.TabularInline):
    model = storage_unit
    extra = 1

class Gpu_unit_inline(admin.TabularInline):
    model = Gpu_unit
    extra = 1

class Case_Fan_unit_inline(admin.TabularInline):
    model = Case_Fan_unit
    extra = 1

class extra_storage_unit_inline(admin.TabularInline):
    model = extra_storage_unit
    extra = 1

class accessory_unit_inline(admin.TabularInline):
    model = accessory_unit
    extra = 1

class optical_drive_unit_inline(admin.TabularInline):
    model = optical_drive_unit
    extra = 1



class Bc_Collection_Admin(admin.ModelAdmin):
    
    inlines  = [memory_unit_inline,storage_unit_inline,Gpu_unit_inline,Case_Fan_unit_inline]
    list_display = ["id","motherboard","cpu"]
    readonly_fields = ["id","population"]
    fieldsets = (
        ("general",{"fields":("id","population","liked")}),
        ("main part",{"fields":("case","motherboard","cpu","PowerSupply")}),
        ("cooling",{"fields":("cpu_cooler","Fan_controller")}),
        ("extentions",{"fields":("SoundCard","WiresNetworkCard","WirelessNetworkCard")})
                 
        )



admin.site.register(BC_Collection,Bc_Collection_Admin)





class Collection_order_Admin(admin.ModelAdmin):
    
    inlines  = [extra_storage_unit_inline,accessory_unit_inline,optical_drive_unit_inline]
    list_display = ["name","client","order_date","state"]
    readonly_fields = ["id","rejected_times","order_date","last_event_date"]
    fieldsets = (
        ("general",{"fields":("id","name","bc","client","cost")}),
        ("order info",{"fields":("order_date","state","last_event_date","rejected_times")}),
        ("order parts",{"fields":("os","thermal_paste","mouse","keyboard","monitor","hradphones","speakers","webcam")})
                 
        )



admin.site.register(Collection_order,Collection_order_Admin)


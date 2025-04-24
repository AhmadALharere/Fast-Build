from django.contrib import admin
from .models import ShopBascet,order,Descount
# Register your models here.




from django.db.models import Exists, OuterRef



class IncompleteOrdersFilter(admin.SimpleListFilter):
    title = "uncomplete bascets"  # عنوان الفلتر في Django Admin
    parameter_name = "incomplete_orders"  # اسم المعامل المستخدم في الاستعلام

    def lookups(self, request, model_admin):
        """
        تحديد القيم التي ستظهر في الفلتر الجانبي
        """
        return [
            ("yes", "yes"),
            ("no", "no")
        ]

    def queryset(self, request, queryset):
        """
        تعديل الاستعلام لتصفية السلال بناءً على الطلبات غير المكتملة
        """
        incomplete_orders = order.objects.filter(bascet=OuterRef("pk")).exclude(state="Done")

        if self.value() == "yes":
            return queryset.annotate(has_incomplete_order=Exists(incomplete_orders)).filter(has_incomplete_order=True).order_by("order_date")
        elif self.value() == "no":
            return queryset.annotate(has_incomplete_order=Exists(incomplete_orders)).filter(has_incomplete_order=False).order_by("order_date")

        return queryset  # إذا لم يتم تحديد فلتر، نعيد جميع السجلات





class inline_order(admin.TabularInline):
    model = order
    extra = 1



class Shop_Bascet_admin(admin.ModelAdmin):
    
    inlines = [inline_order]
    list_display = ["id","client","total_cost"]
    readonly_fields=["id","client","order_date"]
    list_filter = [IncompleteOrdersFilter]
    
    
    
admin.site.register(ShopBascet,Shop_Bascet_admin)
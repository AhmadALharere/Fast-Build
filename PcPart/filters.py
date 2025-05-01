import django_filters
from .models import Part
from django.contrib.contenttypes.models import ContentType

class PartFilter(django_filters.FilterSet):
    part_type = django_filters.CharFilter(method='filter_by_type')
    min_price = django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price',lookup_expr='lte')

    class Meta:
        model = Part
        fields = ['part_type','min_price','max_price']

    def filter_by_type(self, queryset, name, value):
        if not value:
            return queryset

        try:
            # ابحث عن موديل بنفس الاسم (الاسم لازم يتطابق مع الـ model name بالانجليزي الصغير)
            content_type = ContentType.objects.get(model=value.lower())
            return queryset.filter(content_type=content_type)
        except ContentType.DoesNotExist:
            return queryset.none()
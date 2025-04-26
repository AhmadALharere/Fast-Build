from rest_framework import serializers
from .models import ShopBascet,order
from PcPart.models import Part



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Part
        fields=["Gid","name","price","image_filename"]
    


class Cart_Serializer(serializers.ModelSerializer):
    class Meta:
        model=ShopBascet
        fields=["id","order_date","total_cost","state"]
    
    
class OrderSerializer(serializers.ModelSerializer):
    part_detail=ProductSerializer(source='product',read_only=True)
    class Meta:
        model = order
        fields = ['part_detail', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = ShopBascet
        fields = ["id","order_date","total_cost","state","orders"]



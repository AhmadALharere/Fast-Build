from rest_framework import serializers
from .models import Cart,order
from PcPart.models import Part



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Part
        fields=["id","name","price","image_filename"]
    


class Cart_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=["id","order_date","total_cost","statue"]
    
    
class OrderSerializer(serializers.ModelSerializer):
    part_detail=ProductSerializer(source='product',read_only=True)
    class Meta:
        model = order
        fields = ['part_detail', 'quantity']


class BasketSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id","order_date","total_cost","statue","orders"]



from rest_framework import serializers
from PcPart.models import Part

class PartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Part
        fields=['Gid','name','price','population','liked','image_filename']
        
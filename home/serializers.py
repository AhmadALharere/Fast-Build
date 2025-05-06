from rest_framework import serializers
from PcPart.models import Part
from PcPart.serializer import CaseSerializer,CaseAccessorySerializer,CaseFanSerializer,CpuCoolerSerializer,CpuSerializer,VideoCardSerializer,MouseSerializer,ExternalHardDriveSerializer,FanControllerSerializer,headphonesSerializer,InternalHardDriveSerializer,KeyboardSerializer,MemorySerializer,MonitorSerializer,MotherBoardSerializer,OpticalDriveSerializer,PowerSupplySerializer,SoundCardSerializer,SpeakersSerializer,WiresNetworkCardSerializer,WirelessNetworkCardSerializer,WebcamSerializer,ThermalPasteSerializer
from .models import Notification,Like


class PartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Part
        fields=['id','name','price','population','like_count','image_filename']
        

class PartDetailsSerializer(serializers.ModelSerializer):
    
    details = serializers.SerializerMethodField()
    
    class Meta:
        model=Part
        fields = ['id','name','price','population','like_count','image_filename','details']
        
    def get_details(self,obj):
        try:
            value = obj.content_type.model.lower()
            if value=='case':
                return CaseSerializer(obj).data
            elif value=='caseaccessory':
                return CaseAccessorySerializer(obj).data
            elif value=='casefan':
                return CaseFanSerializer(obj).data
            elif value=='cpucooler':
                return CpuCoolerSerializer(obj).data
            elif value=='cpu':
                return CpuSerializer(obj).data
            elif value=='externalharddrive':
                return ExternalHardDriveSerializer(obj).data
            elif value=='fancontroller':
                return FanControllerSerializer(obj).data
            elif value=='headphones':
                return headphonesSerializer(obj).data
            elif value=='internalharddrive':
                return InternalHardDriveSerializer(obj).data
            elif value=='keyboard':
                return KeyboardSerializer(obj).data
            elif value=='memory':
                return MemorySerializer(obj).data
            elif value=='monitor':
                return MonitorSerializer(obj).data
            elif value=='motherBoard':
                return MotherBoardSerializer(obj).data
            elif value=='mouse':
                return MouseSerializer(obj).data
            elif value=='opticaldrive':
                return OpticalDriveSerializer(obj).data
            elif value=='powersupply':
                return PowerSupplySerializer(obj).data
            elif value=='soundcard':
                return SoundCardSerializer(obj).data
            elif value=='speakers':
                return SpeakersSerializer(obj).data
            elif value=='ThermalPaste':
                return ThermalPasteSerializer(obj).data
            elif value=='videocard':
                return VideoCardSerializer(obj).data
            elif value=='webcam':
                return WebcamSerializer(obj).data
            elif value=='wiresnetworkcard':
                return WiresNetworkCardSerializer(obj).data
            elif value=='wirelessnetworkcard':
                return WirelessNetworkCardSerializer(obj).data
            else:
                return None
            
        except Exception as Ex:
            return None
        


class like_Serializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model=Like
        fields = "__all__"
  
  
        
class liked_Part_Serializer(serializers.ModelSerializer):
    part = PartSerializer()
    class Meta:
        model=Like
        fields = ['part','created_at']
        
    
class Notification_serializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        exclude = ['user']
        
    def get_type(self,obj):
        return "Private" if obj.user!=None else "Public"
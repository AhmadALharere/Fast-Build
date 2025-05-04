from rest_framework import serializers
from .models import Case,CaseFan ,motherBoard_Socket, CaseAccessory, Cpu, CpuCooler, ExternalHardDrive, FanController, Form_Factor, headphones, InternalHardDrive, Keyboard, Memory, Monitor, Mouse, MotherBoard, OpticalDrive,  PowerSupply, SoundCard, Speakers,ThermalPaste , VideoCard ,Webcam, WirelessNetworkCard,WiresNetworkCard 




class CaseSerializer(serializers.ModelSerializer):

    build_in_power_supply = serializers.CharField(source='psu')
    form_factor_support = serializers.StringRelatedField(many=True)
    fan_120mm_capacity = serializers.IntegerField(source='fan_120mm_support')
    fan_140mm_capacity = serializers.IntegerField(source='fan_140mm_support')
    external_525_bays = serializers.IntegerField(source='socket5_25')
    internal_35_bays = serializers.IntegerField(source='socket3_5')
    internal_25_bays = serializers.IntegerField(source='socket2_5')
    

    class Meta:
        model=Case
        fields=['type','color','side_panel','build_in_power_supply','form_factor_support','fan_120mm_capacity','fan_140mm_capacity','cpu_cooler_clearance','radiator_support','gpu_clearance','external_525_bays','internal_35_bays','internal_25_bays']    
    
    
    
class CaseAccessorySerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= CaseAccessory
        fields= "__all__"
   
   
         
class ExternalHardDriveSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= ExternalHardDrive
        fields= "__all__"
      
      
class FanControllerSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= FanController
        exclude= ['formFactor']
      

      
class headphonesSerializer(serializers.ModelSerializer):
        
    frequency_Response = serializers.SerializerMethodField(read_only=True)
    is_wireless = serializers.SerializerMethodField(read_only=True)
    enclosure_type = serializers.CharField(source='enclosureType')
    class Meta:
            
        model= headphones
        fields= ['type','microphone','is_wireless','enclosure_type','color','frequency_Response','features']
      
  
    def get_frequency_Response(self,obj):
        return f" {obj.LfrequencyResponse}Hz ~ {obj.UfrequencyResponse}Hz "
   
    
    def get_is_wireless(self,obj):
        return "Yes" if obj.wireless else "No"
   
      
      
class InternalHardDriveSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= InternalHardDrive
        fields= "__all__"
      
      
      
class KeyboardSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= Keyboard
        fields= "__all__"
      
      
      
class MemorySerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= Memory
        fields= "__all__"
      
      
      
class MonitorSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= Monitor
        fields= "__all__"
      
      

class MouseSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= Mouse
        fields= "__all__"
      
      
      
class MotherBoardSerializer(serializers.ModelSerializer):
        
        
    class Meta:
            
        model= MotherBoard
        fields= "__all__"
      
      
      
class OpticalDriveSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= OpticalDrive
        fields= "__all__"
      
      
      
      
class PowerSupplySerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= PowerSupply
        fields= "__all__"
      
      
      
class SoundCardSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= SoundCard
        fields= "__all__"
      
      
      
class SpeakersSerializer(serializers.ModelSerializer):
       
    frequency_Response = serializers.SerializerMethodField(read_only=True)
    
        
    class Meta:
            
        model= Speakers
        fields= ['category','color','configuration','wattage','frequency_Response','features']
      
      
      
    def get_frequency_Response(self,obj):
        return f" {obj.LfrequencyResponse}Hz ~ {obj.UfrequencyResponse}Hz "
  
      
class ThermalPasteSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= ThermalPaste
        fields= "__all__"
      
      
class WebcamSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= Webcam
        fields= "__all__"
      
      
      
class WirelessNetworkCardSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= WirelessNetworkCard
        fields= "__all__"
      
      
      
class WiresNetworkCardSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= WiresNetworkCard
        fields= "__all__"
      
        
        
class CaseFanSerializer(serializers.ModelSerializer):
    
    rpm = serializers.SerializerMethodField()
    airflow = serializers.SerializerMethodField()
    noise_level = serializers.SerializerMethodField()
    
    
    class Meta:
       model = CaseFan
       fields =  ['rpm','airflow','noise_level','size','color','fan_type','compatibility','rgb_support','features']
       
    def get_rpm(self,obj):
        return f" {obj.Lrpm} ~ {obj.Urpm} "
    def get_airflow(self,obj):
        return f" {obj.Lairflow} ~ {obj.Uairflow} "
    def get_noise_level(self,obj):
        return f" {obj.Lnoise_level} ~ {obj.Unoise_level} "
  
        
           
class CpuCoolerSerializer(serializers.ModelSerializer):
    
    rpm = serializers.SerializerMethodField()
    noise_level = serializers.SerializerMethodField()
    
    
    class Meta:
       model = CpuCooler
       fields =  ['color','size','type','rpm','noise_level','compatibility','cooler_height','features']
    
    def get_rpm(self,obj):
        return f" {obj.Lrpm} ~ {obj.Urpm} "
    def get_noise_level(self,obj):
        return f" {obj.Lnoise_level} ~ {obj.Unoise_level} "
  
  
class CpuSerializer(serializers.ModelSerializer):
    socket = serializers.StringRelatedField()
    tdp = serializers.SerializerMethodField()
    cooling_included = serializers.SerializerMethodField()
    Simultaneous_Multithreading = serializers.SerializerMethodField()
    
    
    class Meta:
       model = Cpu
       fields =  ['release_year','socket','core_count','core_clock','boost_clock','tdp','max_memory_support','cooling_included','graphics','Simultaneous_Multithreading']
       
    def get_tdp(self,obj):
        return f"{obj.tdp} W"
    def get_cooling_included(self,obj):
        return "Yes" if obj.cooling_included else "No"
    def get_Simultaneous_Multithreading(self,obj):
        return "Yes" if obj.smt else "No" 
     
  
  
class VideoCardSerializer(serializers.ModelSerializer):
    
    
    class Meta:
       model = VideoCard
       fields = "__all__"
       
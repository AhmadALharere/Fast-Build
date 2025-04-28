from rest_framework import serializers
from .models import Case,CaseFan ,motherBoard_Socket, CaseAccessory, Cpu, CpuCooler, ExternalHardDrive, FanController, Form_Factor, headphones, InternalHardDrive, Keyboard, Memory, Monitor, Mouse, MotherBoard, OpticalDrive,  PowerSupply, SoundCard, Speakers,ThermalPaste , VideoCard ,Webcam, WirelessNetworkCard,WiresNetworkCard 
from .models import Radiator_size


class CeseSerializer(serializers.ModelSerializer):
    
    form_factor_support = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )
    radiator_support = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
    
    class Meta:
       model = Case
       fields =  [
            'name',
            'price',
            'type',
            'color',
            'side_panel',
            'psu',
            'form_factor_support',
            'cpu_cooler_clearance',
            'radiator_support',
            'gpu_clearance',
            'socket5_25',
            'socket3_5',
            'socket2_5',
            'fan_120mm_support',
            'fan_140mm_support',
            
        ]
        
    def create(self, validated_data):
        
        # الحقول الافتراضية
        validated_data['population'] = 0
        validated_data['in_storage'] = 0

        forms_names = validated_data.pop('form_factor_support', [])
        radiator_support_sizes = validated_data.pop('radiator_support', [])
        #print("finish, value : "+validated_data.get("external_525_bays"))
        case = Case.objects.create(**validated_data )
        # Retrieve or create items by their names
        forms = []
        radiators = []
        for name in forms_names:
            item, _ = Form_Factor.objects.get_or_create(name=name)
            forms.append(item)
        for size in radiator_support_sizes:
            item, _ = Radiator_size.objects.get_or_create(size=size)
            radiators.append(item)
        
        case.form_factor_support.set(forms)
        case.radiator_support.set(radiators)
        case.save()
        return case
    
    
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
        fields= "__all__"
      
      
class headphonesSerializer(serializers.ModelSerializer):
        
    class Meta:
            
        model= headphones
        fields= "__all__"
      
      
      
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
        
    class Meta:
            
        model= Speakers
        fields= "__all__"
      
      
      
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
      
        
        
class CeseFanSerializer(serializers.ModelSerializer):
    
    
    class Meta:
       model = CaseFan
       fields =  "__all__"
       
           
           
class CpuCoolerSerializer(serializers.ModelSerializer):
    
    
    class Meta:
       model = CpuCooler
       fields =  "__all__"
    
       
    def create(self, validated_data):
        
        # الحقول الافتراضية
        validated_data['population'] = 0
        validated_data['ammount'] = 10

        #print("finish, value : "+validated_data.get("external_525_bays"))
        cpucooler = CpuCooler.objects.create(**validated_data )
        cpucooler.save()
        return cpucooler
    
  
  
class CpuSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Cpu
       fields =  "__all__"
        
    def create(self, validated_data):
        
        # الحقول الافتراضية
        validated_data['population'] = 0
        validated_data['ammount'] = 10

        socketName = validated_data.pop('socket')
        #print("finish, value : "+validated_data.get("external_525_bays"))
        cpu = Cpu.objects.create(**validated_data )
        # Retrieve or create items by their names
        cpu.socket = motherBoard_Socket.objects.get_or_create(name=socketName)
        cpu.save()
        return cpu
  
  
  
class VideoCardSerializer(serializers.ModelSerializer):
    
    
    class Meta:
       model = VideoCard
       fields = [
           'name',
           'price',
           'chipset',
           'memory',
           'coreClock',
           'boostClock',
           'color',
           'length',
           'interface',
           'power_requirement',
           'compatible_motherboards',
           'release_year'
       ]
        
    def create(self, validated_data):
        
        # الحقول الافتراضية
        validated_data['population'] = 0
        validated_data['ammount'] = 0

        forms_names = validated_data.pop('compatible_motherboards', [])
        #print("finish, value : "+validated_data.get("external_525_bays"))
        videocard = VideoCard.objects.create(**validated_data )
        # Retrieve or create items by their names
        forms = []
        for name in forms_names:
            item, _ = motherBoard_Socket.objects.get_or_create(name=name)
            forms.append(item)
        
        videocard.compatible_motherboards.set(forms)
        videocard.save()
        return videocard

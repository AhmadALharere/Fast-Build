from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# app name: build
class BC_Collection(models.Model):
    
    id = models.AutoField(primary_key=True)
    population = models.IntegerField(default=0)
    liked = models.BigIntegerField(default=0)
    motherboard = models.ForeignKey("PcPart.MotherBoard", on_delete=models.CASCADE)
    case = models.ForeignKey("PcPart.Case", on_delete=models.CASCADE)
    cpu = models.ForeignKey("PcPart.Cpu", on_delete=models.CASCADE)
    cpu_cooler = models.ForeignKey("PcPart.CpuCooler", on_delete=models.CASCADE)
    memory = models.ManyToManyField("PcPart.Memory",through="memory_unit")
    storage = models.ManyToManyField("PcPart.InternalHardDrive", through="storage_unit")
    gpus = models.ManyToManyField("PcPart.VideoCard", through="Gpu_unit")
    SoundCard = models.ForeignKey("PcPart.SoundCard",null=True,blank=True, on_delete=models.CASCADE)
    WiresNetworkCard = models.ForeignKey("PcPart.WiresNetworkCard",null=True,blank=True, on_delete=models.CASCADE)
    WirelessNetworkCard = models.ForeignKey("PcPart.WirelessNetworkCard",null=True,blank=True, on_delete=models.CASCADE)
    fans = models.ManyToManyField("PcPart.CaseFan", through="Case_Fan_unit")
    Fan_controller = models.ForeignKey("PcPart.FanController",null=True,blank=True, on_delete=models.CASCADE)
    PowerSupply = models.ForeignKey("PcPart.PowerSupply",null=True,blank=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"collection #{self.id}"
   
   
   

class memory_unit(models.Model):
    
    BC = models.ForeignKey(BC_Collection, on_delete=models.CASCADE)
    unit = models.ForeignKey("PcPart.Memory", on_delete=models.CASCADE)
    unit_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.unit.__str__()
        
    
 

   
 
class storage_unit(models.Model):
    
    BC = models.ForeignKey(BC_Collection, on_delete=models.CASCADE)
    unit = models.ForeignKey("PcPart.InternalHardDrive", on_delete=models.CASCADE)
    unit_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.unit.__str__()
    
    
    
    
    
class Gpu_unit(models.Model):
    
    BC = models.ForeignKey(BC_Collection, on_delete=models.CASCADE)
    unit = models.ForeignKey("PcPart.VideoCard", on_delete=models.CASCADE)
    unit_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.unit.__str__()
    
    
    
    
class Case_Fan_unit(models.Model):
    
    BC = models.ForeignKey(BC_Collection, on_delete=models.CASCADE)
    unit = models.ForeignKey("PcPart.CaseFan", on_delete=models.CASCADE)
    unit_count = models.IntegerField(default=1)
    
    def __str__(self):
        return self.unit.__str__()
    
    
    
state_list = (
    ("Waiting","Waiting"),
    ("Ready","Ready"),
    ("Done","Done"),
    ("Canceled","Canceled"),
    ("Rejected","Rejected")
    
)
    
    
class Collection_order(models.Model):
    
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=75)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    bc = models.ForeignKey("BC_Collection", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    state = models.CharField(default="Waiting",choices=state_list, max_length=20)
    last_event_date = models.DateTimeField(auto_now_add=True)
    rejected_times = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    os = models.ForeignKey("PcPart.OS", on_delete=models.CASCADE)
    thermal_paste = models.ForeignKey("PcPart.ThermalPaste", on_delete=models.CASCADE)
    mouse = models.ForeignKey("PcPart.Mouse", on_delete=models.CASCADE,null=True,blank=True)
    keyboard = models.ForeignKey("PcPart.Keyboard", on_delete=models.CASCADE,null=True,blank=True)
    monitor = models.ForeignKey("PcPart.Monitor", on_delete=models.CASCADE,null=True,blank=True)
    hradphones = models.ForeignKey("PcPart.Headphones", on_delete=models.CASCADE,null=True,blank=True)
    speakers = models.ForeignKey("PcPart.Speakers", on_delete=models.CASCADE,null=True,blank=True)
    webcam = models.ForeignKey("PcPart.Webcam", on_delete=models.CASCADE,null=True,blank=True)
    EHD = models.ManyToManyField("PcPart.ExternalHardDrive",through="extra_storage_unit",blank=True)
    accessorys = models.ManyToManyField("PcPart.CaseAccessory",through="accessory_unit",blank=True)
    optical_drive = models.ManyToManyField("PcPart.OpticalDrive",through="optical_drive_unit",blank=True)
    
    
    def __str__(self):
        return self.name.__str__()
    
    
class extra_storage_unit(models.Model):
    
    order = models.ForeignKey(Collection_order, on_delete=models.CASCADE)
    unit = models.ForeignKey("PcPart.ExternalHardDrive", on_delete=models.CASCADE)
    unit_count = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.unit.__str__()
    
    
class accessory_unit(models.Model):
    
        order = models.ForeignKey(Collection_order, on_delete=models.CASCADE)
        unit = models.ForeignKey("PcPart.CaseAccessory", on_delete=models.CASCADE)
        unit_count = models.IntegerField(default=1)
        
        
        def __str__(self):
            return self.unit.__str__()
        
    
    
class optical_drive_unit(models.Model):
    
        order = models.ForeignKey(Collection_order, on_delete=models.CASCADE)
        unit = models.ForeignKey("PcPart.OpticalDrive", on_delete=models.CASCADE)
        unit_count = models.IntegerField(default=1)
        
        
        def __str__(self):
            return self.unit.__str__()
        
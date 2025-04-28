from django.contrib import admin
from .models import Case,CaseFan ,motherBoard_Socket, CaseAccessory, Cpu, CpuCooler, ExternalHardDrive, FanController, Form_Factor, headphones, InternalHardDrive, Keyboard, Memory, Monitor, Mouse, MotherBoard, OpticalDrive, PowerSupply, SoundCard, Speakers,ThermalPaste , VideoCard ,Webcam, WirelessNetworkCard,WiresNetworkCard 
from .models import Radiator_size
# Register your models here.


admin.site.register(Case)

admin.site.register(CaseFan)

admin.site.register(CaseAccessory)

admin.site.register(motherBoard_Socket)

admin.site.register(Cpu)

admin.site.register(CpuCooler)

admin.site.register(ExternalHardDrive)

admin.site.register(FanController)
admin.site.register(Form_Factor)

admin.site.register(headphones)

admin.site.register(InternalHardDrive)

admin.site.register(Keyboard)

admin.site.register(Memory)

admin.site.register(Monitor)

admin.site.register(Mouse)

admin.site.register(MotherBoard)

admin.site.register(OpticalDrive)

admin.site.register(PowerSupply)

admin.site.register(SoundCard)

admin.site.register(Speakers)

admin.site.register(ThermalPaste)

admin.site.register(VideoCard)

admin.site.register(Webcam)
admin.site.register(WirelessNetworkCard)
admin.site.register(WiresNetworkCard)
admin.site.register(Radiator_size)

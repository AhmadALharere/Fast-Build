from django.urls import path

from . import api


urlpatterns = [
    path('load Cases From File', api.load_Cases,name="LoadCases"),
    path('load Case Accessorys From File', api.load_Case_accessorys,name="LoadCasesAccessory"),
    path('load Case Fans From File', api.load_Case_Fans,name="LoadCasesFan"),
    path('load Cpu Coolers From File', api.load_Cpu_Cooler,name="LoadCpuCooler"),
    path('load Cpus From File', api.load_Cpus,name="LoadCpus"),
    path('load EHD From File', api.load_External_Hard_Drive,name="LoadExternalHardDrive"),
    path('load IHD From File', api.load_Internal_Hard_Drive,name="LoadInternalHardDrive"),
    path('load Fan Controller From File', api.load_Fan_Controller,name="LoadFanController"),
    path('load Headphones From File', api.load_Headphones,name="LoadHeadphones"),
    path('load Keyboard From File', api.load_Keyboard,name="LoadKeyboard"),
    path('load Memory From File', api.load_Memory,name="LoadMemory"),
    path('load Monitor From File', api.load_Monitor,name="LoadMonitor"),
    path('load MotherBoard From File', api.load_MotherBoard,name="LoadMotherBoard"),
    path('load Mouse From File', api.load_Mouse,name="LoadMouse"),
    path('load OpticalDrive From File', api.load_OpticalDrive,name="LoadOpticalDrive"),
    path('load PowerSupply From File', api.load_PowerSupply,name="LoadPowerSupply"),
    path('load SoundCard From File', api.load_SoundCard,name="LoadSoundCard"),
    path('load Speakers From File', api.load_Speakers,name="LoadSpeakers"),
    path('load ThermalPaste From File', api.load_ThermalPaste,name="LoadThermalPaste"),
    path('load VideoCard From File', api.load_VideoCard,name="LoadVideoCard"),
    path('load Webcam From File', api.load_Webcam,name="LoadWebcam"),
    path('load WiresNetworkCard From File', api.load_WiresNetworkCard,name="LoadWiresNetworkCard"),
    path('load WirelessNetworkCard From File', api.load_WirelessNetworkCard,name="LoadWirelessNetworkCard"),
    path('R/<int:id>', api.RCaseAcc.as_view(),name="Ret"),
    path('Reset', api.reset_dataBase,name="Reset Data"),
    #path('download image', api.download_high_res_image,name="downloadImage"),
    #path('Count Cases', api.countCases,name="CountCases"),
#    path('admin/', admin.site.urls),
]

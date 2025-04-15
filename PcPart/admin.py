from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Case,CaseFan ,motherBoard_Socket, CaseAccessory, Cpu, CpuCooler, ExternalHardDrive, FanController, Form_Factor, headphones, InternalHardDrive, Keyboard, Memory, Monitor, Mouse, MotherBoard, OpticalDrive, OS, PowerSupply, SoundCard, Speakers,ThermalPaste , VideoCard ,Webcam, WirelessNetworkCard,WiresNetworkCard 
from .models import Radiator_size
# Register your models here.



@admin.action(description="Empty storage")
def empty_Storage(modeladmin,request,queryset):
    queryset.update(in_storage = 0)
    modeladmin.message_user(request, f"Empty storage for {queryset.count()} parts done successfully")


class Fan_Noise_Filter(admin.SimpleListFilter):
    title = "filter by max noise level:"
    parameter_name = "Unoise_level"
    
    def lookups(self, request, model_admin):
        return [
        ("ultra_silent", "Ultra-Silent (less than 15db)"),
        ("silent", "Silent (15db-25db)"),
        ("moderate", "Moderate Noise (25db-35db)"),
        ("loud", "Loud (35db-45db)"),
        ("very_loud", "Very Loud (more than 45db)")
        ]
    def queryset(self, request, queryset):
        
        if self.value()=="ultra_silent":
            return queryset.filter(Unoise_level__lt=15)
        if self.value()=="silent":
            return queryset.filter(Unoise_level__lt=25,Unoise_level__gte=15)
        if self.value()=="moderate":
            return queryset.filter(Unoise_level__lt=35,Unoise_level__gte=25)
        if self.value()=="loud":
            return queryset.filter(Unoise_level__lt=45,Unoise_level__gte=35)
        if self.value()=="very_loud":
            return queryset.filter(Unoise_level__gt=45)
    

class Fan_Rounds_Rate_filter(admin.SimpleListFilter):
    title = "filter by max Round Rate:"
    parameter_name = "Urpm"
    
    def lookups(self, request, model_admin):
        return [
        ("Ultra-Low", "Ultra-Low RPM (less than 800 RPM)"),
        ("Low", "Low RPM (800-1200 RPM)"),
        ("moderate", "Moderate  RPM (1200-1800 RPM)"),
        ("High", "High RPM (1800-2500 RPM)"),
        ("Ultra-High", "Ultra-High RPM(more than 2500 RPM)")
        ]
    def queryset(self, request, queryset):
        
        if self.value()=="Ultra-Low":
            return queryset.filter(Urpm__lt=800)
        if self.value()=="Low":
            return queryset.filter(Urpm__lt=1200,Urpm__gte=800)
        if self.value()=="moderate":
            return queryset.filter(Urpm__lt=1800,Urpm__gte=1200)
        if self.value()=="High":
            return queryset.filter(Urpm__lt=2500,Urpm__gte=1800)
        if self.value()=="Ultra-High":
            return queryset.filter(Urpm__gt=2500)
 


class CaseAdmin(admin.ModelAdmin):
    
    
    
    search_fields = ("name","type")
    readonly_fields = ["population","Gid"]
    list_filter = ["form_factor_support"]
    list_display = ("name","type")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","type","color","side_panel")}),
        ("power info", {"fields": ["psu"]}),
        ("motherBoard compatibility", {"fields": ["form_factor_support"]}),
        ("cooling capcacity", {"fields": ("fan_120mm_support", "fan_140mm_support","cpu_cooler_clearance","radiator_support")}),
        ("Video Card compatibility", {"fields": ["gpu_clearance"]}),
        ("Storage socket", {"fields": ("socket5_25", "socket3_5","socket2_5")})
    	)    


admin.site.register(Case,CaseAdmin)


class CaseFanAdmin(admin.ModelAdmin):
    
    
    
    search_fields = ("name","compatibility","features")
    readonly_fields = ["population","Gid"]
    list_filter = ["size","fan_type","rgb_support","pwm",Fan_Noise_Filter,Fan_Rounds_Rate_filter]
    list_display = ("name","fan_type")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","size","fan_type","color")}),
        ("Round Per Minite", {"fields": ["Lrpm","Urpm","pwm"]}),
        ("airflow", {"fields": ["Lairflow","Uairflow"]}),
        ("noise level", {"fields": ["Lnoise_level","Unoise_level"]}),
        ("other Statues info", {"fields": ["compatibility","features","rgb_support"]})
        
    	)    


admin.site.register(CaseFan,CaseFanAdmin)



class CaseAccessoryAdmin(admin.ModelAdmin):
    
    
    
    search_fields = ("name","compatibility","features")
    readonly_fields = ["population","Gid"]
    list_filter = ["type","form_factor","power_requirement"]
    list_display = ("name","type")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","type")}),
        ("Case", {"fields": ["compatibility","form_factor"]}),
        ("power", {"fields": ["power_requirement"]}),
        ("other Statues info", {"fields": ["features"]})
        
    	)    


admin.site.register(CaseAccessory,CaseAccessoryAdmin)


admin.site.register(motherBoard_Socket)


class CpuAdmin(admin.ModelAdmin):
    
    search_fields = ["name","graphics"]
    readonly_fields = ["population","Gid"]
    list_filter = ["release_year","socket","core_count"]
    list_display = ("name","socket","core_clock","boost_clock")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","release_year")}),
        ("socket", {"fields": ["socket"]}),
        ("core info", {"fields": ["core_count","core_clock","boost_clock"]}),
        ("power", {"fields": ["tdp"]}),
        ("memory", {"fields": ["max_memory_support"]}),
        ("cooling info", {"fields": ["cooling_included"]}),
        ("GPU", {"fields": ["graphics","integrated_graphics"]}),
        ("Simultaneous Multithreading", {"fields": ["smt"]})
        
        
    	)    


admin.site.register(Cpu,CpuAdmin)


class CpuCoolerAdmin(admin.ModelAdmin):
    
    search_fields = ["name","compatibility","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["size","cooler_height",Fan_Noise_Filter,Fan_Rounds_Rate_filter]
    list_display = ("name","type","size","cooler_height")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","size","type","cooler_height")}),
        ("Round per Minite", {"fields": ["Lrpm","Urpm"]}),
        ("noise level", {"fields": ["Lnoise_level","Unoise_level"]}),
        ("Other info", {"fields": ["compatibility","features"]})
        
        
    	)    


admin.site.register(CpuCooler,CpuCoolerAdmin)


class EHDAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["color","interface"]
    list_display = ("name","type","Space","interface")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","pricePerGB")}),
        ("statues info", {"fields": ["type","interface","capacity","max_speed"]}),
        ("Other info", {"fields": ["features"]})
    	)    

    def Space(self,obj):
        return f"{obj.capacity} GB"

admin.site.register(ExternalHardDrive,EHDAdmin)

class Fan_controlller_Admin(admin.ModelAdmin):
    
    search_fields = ["name","features","compatibility"]
    readonly_fields = ["population","Gid"]
    list_filter = ["formFactor","pwm","channels"]
    list_display = ("name","max_power","pwm")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","formFactor")}),
        ("channels info", {"fields": ["channels","channelsWattage"]}),
        ("round controller", {"fields": ["pwm"]}),
        ("power info", {"fields": ["max_power"]}),
        ("Other info", {"fields": ["features","compatibility"]})
    	)    

   
admin.site.register(FanController,Fan_controlller_Admin)
admin.site.register(Form_Factor)


class HeadphonesAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["type","microphone","wireless","enclosureType"]
    list_display = ("name","Low_frequency_Response","High_frequency_Response")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","type")}),
        ("frequency Response", {"fields": ["LfrequencyResponse","UfrequencyResponse"]}),
        ("Other info", {"fields": ["microphone","wireless","enclosureType","features"]})
    	)    

    def Low_frequency_Response(self,obj):
        return f"{obj.LfrequencyResponse} Hz"

    def High_frequency_Response(self,obj):
        return f"{obj.UfrequencyResponse} Hz"



admin.site.register(headphones,HeadphonesAdmin)


class IHDAdmin(admin.ModelAdmin):
    
    search_fields = ["name","type","interface"]
    readonly_fields = ["population","Gid"]
    list_filter = ["type","formFactor"]
    list_display = ("name","type","Space","interface")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","pricePerGB")}),
        ("statues info", {"fields": ["type","interface","capacity","cache","formFactor"]}),
        ("Other info", {"fields": ["features"]})
    	)    

    def Space(self,obj):
        return f"{obj.capacity} GB"


admin.site.register(InternalHardDrive,IHDAdmin)


class KeyboardAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["style","connectionType","backlit","tenkeyless"]
    list_display = ("name","color")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","style","connectionType")}),
        ("Other info", {"fields": ["backlit","switches","tenkeyless","features"]})
    	)    

    


admin.site.register(Keyboard,KeyboardAdmin)


class MemoryAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["generation","total_capacity"]
    list_display = ("name","generation","total_capacity","speed")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","pricePerGB","in_storage","population","color","generation","speed")}),
        ("modules and capacity", {"fields": ["unit_number","unit_capacity","total_capacity"]}),
        ("Other info", {"fields": ["features"]})
    	)    



admin.site.register(Memory,MemoryAdmin)


class MonitorAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["resolution","aspectRatio"]
    list_display = ("name","resolution","refreshRate","screenSize")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population")}),
        ("Desplay info", {"fields": ["screenSize","resolution","refreshRate","responseTime","aspectRatio"]}),
        ("Other info", {"fields": ["features","panelType"]})
    	)    



admin.site.register(Monitor,MonitorAdmin)


class MouseAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["connectionType","hand_orientation","tracking_method"]
    list_display = ("name","color")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","max_dpi","connectionType","color")}),
        ("Other info", {"fields": ["features","tracking_method","hand_orientation"]})
    	)    


admin.site.register(Mouse,MouseAdmin)


class MotherBoardAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["form_Factor","socket","supported_ddr_version","memory_channels","aio_support","rgb_support"]
    list_display = ("name","form_Factor","max_Memory")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","release_year")}),
        ("CPU socket", {"fields": ["socket","cpu_compatibility"]}),
        ("size and form", {"fields": ["form_Factor"]}),
        ("Memory", {"fields": ["memory_Slots","max_capacity_per_slot","max_Memory","supported_ddr_version","supported_memory_frequencies","xmp_support","memory_channels"]}),
        ("storage", {"fields": ["sata_ports","m2_slut"]}),
        ("network and audio", {"fields": ["Lan_network","wifi_network","audio_chipset"]}),
        ("power and cooling support", {"fields": ["power_phases","fan_headers","aio_support"]}),
        ("extansion_capabilities", {"fields": ["usb_2","usb_3","usb_C","pci_slots","pcie_x1_slots","pcie_x4_slots","pcie_x8_slots","pcie_x16_slots"]}),
        ("Other info", {"fields": ["additional_features","rgb_support"]})
    	)    




admin.site.register(MotherBoard,MotherBoardAdmin)


class OpticalDriveAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population")}),
        ("blu-ray", {"fields": ["bd","bd_write"]}),
        ("dvd", {"fields": ["dvd","dvd_write"]}),
        ("cd", {"fields": ["cd","cd_write"]}),
        ("Other info", {"fields": ["features"]})
    	)    



admin.site.register(OpticalDrive,OpticalDriveAdmin)


class OSAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","id"]
    list_filter = ["mode"]
    list_display = ("name","mode","max_memory")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("id","name", "price","population")}),
        ("Other info", {"fields": ["mode","max_memory","features"]})
    	)    


admin.site.register(OS,OSAdmin)


class PowerSupplyAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["type","efficiency","multi_gpu_support","modular"]
    list_display = ("name","wattage","modular")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","type","efficiency","wattage","dimensions")}),
        ("connectors", {"fields": ["ATX_24pin_connectors","EPS_8pin_connectors","PCIe_6_Pls_2pin_connectors","SATA_connectors","Molex_connectors"]}),
        ("multi GBU", {"fields": ["multi_gpu_support"]}),
        ("Other info", {"fields": ["features","modular"]})
    	)    


admin.site.register(PowerSupply,PowerSupplyAdmin)


class SoundCardAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["channels","interface"]
    list_display = ("name","snr","digital_audio")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","interface")}),
        ("audio info", {"fields": ["digital_audio","channels","snr","sample_rate"]}),
        ("Other info", {"fields": ["features","chipset"]})
    	)    



admin.site.register(SoundCard,SoundCardAdmin)


class SpeakersAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_display = ("name","configuration","Ufrequency_response")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","configuration")}),
        ("frequency and wattage", {"fields": ["wattage","Lfrequency_response","Ufrequency_response"]}),
        ("Other info", {"fields": ["features"]})
    	)    




admin.site.register(Speakers,SpeakersAdmin)


admin.site.register(ThermalPaste)



class VideoCardAdmin(admin.ModelAdmin):
    
    search_fields = ["name","chipset"]
    readonly_fields = ["population","Gid"]
    list_filter = ["GRAM","interface"]
    list_display = ("name","chipset","power_requirement","coreClock","boostClock")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","color","GRAM","length","interface")}),
        ("power and chips", {"fields": ["chipset","power_requirement"]}),
        ("core info", {"fields": ["coreClock","boostClock"]}),
        ("Other info", {"fields": ["release_year"]})
    	)    



admin.site.register(VideoCard,VideoCardAdmin)


class WebcamAdmin(admin.ModelAdmin):
    
    search_fields = ["name","features"]
    readonly_fields = ["population","Gid"]
    list_filter = ["resolutions","focus_type"]
    list_display = ("name","resolutions","fov","os")
    actions = [empty_Storage]
    fieldsets = (
        ("General", {"fields": ("Gid","name", "price","in_storage","population","os","connection")}),
        ("camera info", {"fields": ["resolutions","focus_type","fov"]}),
        ("Other info", {"fields": ["features"]})
    	)    



admin.site.register(Webcam,WebcamAdmin)
admin.site.register(WirelessNetworkCard)
admin.site.register(WiresNetworkCard)
admin.site.register(Radiator_size)

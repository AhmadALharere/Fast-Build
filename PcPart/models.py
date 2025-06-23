from django.db import models
from model_utils.managers import InheritanceManager
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
# Create your models here.
#app name: PcPart
#----------------------------------------------------------------------------------------------------

def imageSaver(instance,filename):
    idx = filename.rfind('.')
    if idx <= 0:
         extention = filename[idx:]
    else:
        extention = 'jpg'
    return "PcPart/%s/imgicon/%s.%s"%(instance.content_type.name,instance.id,extention)




ExternalHardDrive_type = (
    ("Portable","Portable"),
    ("Desktop","Desktop")
)

InternalHardDrive_type = (
    ("HDD SATA","HDD SATA"),
    ("HDD SAS","HDD SAS"),
    ("SSD SATA","SSD SATA"),
    ("SSD SAS","SSD SAS"),
    ("SSD NVMe","SSD NVMe"),
    ("SSD M.2","SSD M.2"),
    ("SSD U.2","SSD U.2")
)

InternalHardDrive_interface = (
    ("M.2 PCIe 2.0 X4", "M.2 PCIe 2.0 X4"),
    ("M.2 PCIe 3.0 X2", "M.2 PCIe 3.0 X2"),
    ("M.2 PCIe 3.0 X4", "M.2 PCIe 3.0 X4"),
    ("M.2 PCIe 4.0 X4", "M.2 PCIe 4.0 X4"),
    ("M.2 PCIe 5.0 X4", "M.2 PCIe 5.0 X4"),
    ("M.2 SATA", "M.2 SATA"),
    ("PATA 100", "PATA 100"),
    ("PATA 44-Pin 100", "PATA 44-Pin 100"),
    ("PATA 44-Pin 133", "PATA 44-Pin 133"),
    ("PCIe x1", "PCIe x1"),
    ("PCIe x16", "PCIe x16"),
    ("PCIe x2", "PCIe x2"),
    ("PCIe x4", "PCIe x4"),
    ("PCIe x8", "PCIe x8"),
    ("SAS 12.0 Gb/s", "SAS 12.0 Gb/s"),
    ("SAS 3.0 Gb/s", "SAS 3.0 Gb/s"),
    ("SAS 6.0 Gb/s", "SAS 6.0 Gb/s"),
    ("SATA 1.5 Gb/s", "SATA 1.5 Gb/s"),
    ("SATA 3.0 Gb/s", "SATA 3.0 Gb/s"),
    ("SATA 6.0 Gb/s", "SATA 6.0 Gb/s"),
    ("U.2", "U.2"),
    ("mSATA", "mSATA")
)

type_to_interfaces = {
    "HDD SATA": ["SATA 1.5 Gb/s", "SATA 3.0 Gb/s", "SATA 6.0 Gb/s"],
    "HDD SAS": ["SAS 3.0 Gb/s", "SAS 6.0 Gb/s", "SAS 12.0 Gb/s"],
    "SSD SATA": ["SATA 1.5 Gb/s", "SATA 3.0 Gb/s", "SATA 6.0 Gb/s", "mSATA"],
    "SSD SAS": ["SAS 3.0 Gb/s", "SAS 6.0 Gb/s", "SAS 12.0 Gb/s"],
    "SSD NVMe": [
        "M.2 PCIe 2.0 X4", "M.2 PCIe 3.0 X2", "M.2 PCIe 3.0 X4",
        "M.2 PCIe 4.0 X4", "M.2 PCIe 5.0 X4", "PCIe x1",
        "PCIe x2", "PCIe x4", "PCIe x8", "PCIe x16"
    ],
    "SSD M.2": [
        "M.2 PCIe 2.0 X4", "M.2 PCIe 3.0 X2", "M.2 PCIe 3.0 X4",
        "M.2 PCIe 4.0 X4", "M.2 PCIe 5.0 X4", "M.2 SATA"
    ],
    "SSD U.2": ["U.2"]
}

Fan_Size = (
    (40,"40mm"),
    (50,"50mm"),
    (60,"60mm"),
    (70,"70mm"),
    (80,"80mm"),
    (90,"90mm"),
    (92,"92mm"),
    (95,"95mm"),
    (120,"120mm"),
    (140,"140mm"),
    (180,"180mm"),
    (193,"193mm"),
    (200,"200mm"),
    (220,"220mm"),
    (230,"230mm"),
    (240,"240mm"),
    (250,"250mm"),
    (280,"280mm"),
)

Form_Factor_in_Case = (
    ("5.25",5.25),
    ("3.5",3.5),
    ("2.5",2.5)
)

Fan_Type =(
    ("Standard","Standard"),
    ("Static Pressure","Static Pressure"),
    ("High Airflow","High Airflow"),
    ("Silent","Silent"),
    ("RGB/ARGB","RGB/ARGB"),
    ("Slim","Slim"),
    ("Industrial","Industrial")
) # Standard , Static Pressure , High Airflow , Silent , RGB/ARGB , Slim , Industrial

Cpu_Fan_Type =(
    ("Air Cooler","Air Cooler"),
    ("Liquid Cooler","Liquid Cooler"),
    ("Passive  Cooler","Passive  Cooler"),
    ("Hybrid Cooler","Hybrid Cooler"),
    ("Sub-Ambient Cooler","Sub-Ambient Cooler"),
    ("Airflow Fan ","Airflow Fan"),
    ("VGA Cooler ","VGA Cooler"),
    ("Chipset Cooler","Chipset Cooler"),
    ("Server Cooler","Server Cooler")
) # Air Cooler , Liquid Cooler , Passive  Cooler , Hybrid Cooler , Sub-Ambient Cooler

headphones_Type = (
    ("Circumaural","Circumaural"),
    ("Supra-Aural","Supra-Aural"),
    ("Earbud","Earbud"),
    ("In Ear","In Ear")
)#Circumaural , Supra-Aural , Earbud , In Ear

headphones_enclosureType = (
    ("Open","Open"),
    ("Closed","Closed"),
    ("Semi-Open","Semi-Open")
) 
 
resolutions = (
    ("640x480", "VGA"),  # VGA
    ("800x600", "SVGA"),  # SVGA
    ("1024x768", "XGA"),  # XGA
    ("1280x720", "HD : 1280x720"),  # HD
    ("1280x800", "WXGA"),  # WXGA
    ("1366x768", "HD : 1366x768"),  # HD
    ("1440x900", "WXGA+"),  # WXGA+
    ("1600x900", "HD+"),  # HD+
    ("1680x1050", "WSXGA+"),  # WSXGA+
    ("1920x1080", "Full HD"),  # Full HD
    ("1920x1200", "WUXGA"),  # WUXGA
    ("2560x1080", "UltraWide Full HD"),  # UltraWide Full HD
    ("2560x1440", "QHD / 2K"),  # QHD / 2K
    ("3440x1440", "UltraWide QHD"),  # UltraWide QHD
    ("3840x1600", "UltraWide WQHD+"),  # UltraWide WQHD+
    ("3840x2160", "4K UHD"),  # 4K UHD
    ("5120x1440", "Super UltraWide"),  # Super UltraWide
    ("5120x2880", "5K"),  # 5K
    ("7680x4320", "8K UHD")   # 8K UHD
)
 
cam_Resolutions = (
    ("4k", "4k"),  
    ("2k", "2k"),  
    ("1080p", "1080p"),  
    ("720p", "720p"), 
    ("480p", "480p"), 
    ("360p", "360p"), 
    ("240p", "240p") 
)#"4k","1080p","720p"...
 
memory_channels_list = ( # 4K UHD
    ("Single Channel", "Single Channel"),
    ("Dual Channel", "Dual Channel"),
    ("Quad Channel", "Quad Channel")
    ) 

ddr_versions = (
    ("DDR", "DDR"),              # DDR1 - أول إصدار
    ("DDR2", "DDR2"),            # DDR2
    ("DDR3", "DDR3"),            # DDR3
    ("DDR3L", "DDR3L"),          # DDR3 Low Voltage
    ("DDR4", "DDR4"),            # DDR4
    ("DDR4L", "DDR4L"),          # DDR4 Low Voltage
    ("DDR5", "DDR5"),            # DDR5 - أحدث إصدارات DDR
    ("LPDDR", "LPDDR"),          # Low Power DDR
    ("LPDDR2", "LPDDR2"),        # LPDDR2
    ("LPDDR3", "LPDDR3"),        # LPDDR3
    ("LPDDR4", "LPDDR4"),        # LPDDR4
    ("LPDDR4X", "LPDDR4X"),      # LPDDR4X (تحسين لـ LPDDR4)
    ("LPDDR5", "LPDDR5"),        # LPDDR5
    ("LPDDR5X", "LPDDR5X")       # LPDDR5X (تحسين لـ LPDDR5)
)

mouse_tracking_methods = (
    ("Optical", "Optical"),  
    ("Laser", "Laser"),      
    ("Trackball", "Trackball"),    
    ("Touchpad", "Touchpad")       
)
##Touchpad , Optical , Laser , Trackball
 
mouse_hand_orientation = (
     ("Both", "Both"),      
    ("Right", "Right"),        
    ("Left", "Left")
 )
##Both , Right , Left 

connection_types = (
    ("Wired", "Wired"),      
    ("Wireless", "Wireless"),        
    ("Bluetooth Wireless", "Bluetooth Wireless")
)
##Wired , Wireless , Bluetooth Wireless
 
Extention_Cards_interface = (
    ("PCIe x1", "PCIe x1"),
    ("PCIe x2", "PCIe x2"),
    ("PCIe x4", "PCIe x4"),
    ("PCIe x8", "PCIe x8"),
    ("PCIe x16", "PCIe x16")
) 

focus_types = (
    ("Manual", "Manual"),
    ("Auto", "Auto"),
    ("Fixed", "Fixed")
)#Manual , Auto , Fixed
'''
case_types = (
    ("ATX Mid Tower", "ATX Mid Tower"),
    ("MicroATX Mini Tower", "MicroATX Mini Tower"),
    ("ATX Full Tower", "ATX Full Tower"),
    ("MicroATX Mid Tower", "MicroATX Mid Tower"),
    ("ATX Desktop", "ATX Desktop"),
    ("MicroATX Desktop", "MicroATX Desktop"),
    ("ATX Cube", "ATX Cube"),
    ("MicroATX Cube", "MicroATX Cube"),
    ("ATX HTPC", "ATX HTPC"),
    ("MicroATX HTPC", "MicroATX HTPC"),
    ("ATX Test Bench", "ATX Test Bench"),
    ("MicroATX Test Bench", "MicroATX Test Bench"),
    ("ATX Rackmount", "ATX Rackmount"),
    ("MicroATX Rackmount", "MicroATX Rackmount"),
    ("Mini-ITX Tower", "Mini-ITX Tower"),
    ("Mini-ITX Desktop", "Mini-ITX Desktop"),
    ("Mini-ITX Cube", "Mini-ITX Cube"),
    ("Mini-ITX HTPC", "Mini-ITX HTPC"),
    ("Mini-ITX Test Bench", "Mini-ITX Test Bench"),
    ("Mini-ITX Rackmount", "Mini-ITX Rackmount")
)
'''
case_types = (
    ("ATX Mid Tower", "ATX Mid Tower"),
    ("MicroATX Mini Tower", "MicroATX Mini Tower"),
    ("ATX Full Tower", "ATX Full Tower"),
    ("MicroATX Mid Tower", "MicroATX Mid Tower"),
    ("ATX Desktop", "ATX Desktop"),
    ("MicroATX Desktop", "MicroATX Desktop"),
    ("ATX Cube", "ATX Cube"),
    ("MicroATX Cube", "MicroATX Cube"),
    ("ATX HTPC", "ATX HTPC"),
    ("MicroATX HTPC", "MicroATX HTPC"),
    ("ATX Test Bench", "ATX Test Bench"),
    ("MicroATX Test Bench", "MicroATX Test Bench"),
    ("ATX Rackmount", "ATX Rackmount"),
    ("MicroATX Rackmount", "MicroATX Rackmount"),
    ("Mini-ITX Tower", "Mini-ITX Tower"),
    ("Mini-ITX Desktop", "Mini-ITX Desktop"),
    ("Mini-ITX Cube", "Mini-ITX Cube"),
    ("Mini-ITX HTPC", "Mini-ITX HTPC"),
    ("Mini-ITX Test Bench", "Mini-ITX Test Bench"),
    ("Mini-ITX Rackmount", "Mini-ITX Rackmount")
)

'''
    ATX
    Micro ATX
    Mini ITX
    Thin Mini ITX
    Mini DTX
    Flex ATX
    EATX
    XL ATX
    HPTX
    SSI CEB
    SSI EEB
    '''

power_supply_and_cases = {
    "ATX": [
        "ATX Mid Tower",
        "MicroATX Mini Tower",
        "ATX Full Tower",
        "MicroATX Mid Tower",
        "ATX Desktop",
        "MicroATX Desktop",
        "ATX Cube",
        "MicroATX Cube",
        "ATX HTPC",
        "MicroATX HTPC",
        "ATX Test Bench",
        "MicroATX Test Bench",
        "ATX Rackmount",
        "MicroATX Rackmount"
    ],
    "SFX": [
        "Mini-ITX Tower",
        "Mini-ITX Desktop",
        "Mini-ITX Cube",
        "Mini-ITX HTPC",
        "Mini-ITX Test Bench",
        "Mini-ITX Rackmount"
    ]
}

power_supply_Modular = (
    ("Full", "Full"),
    ("Semi", "Semi"),
    ("False", "False")
)

power_supply_efficiency = (
    ("Unrated", "Unrated"),
    ("Plus", "Plus"),
    ("Bronze", "Bronze"),
    ("Gold", "Gold"),
    ("Platinum", "Platinum"),
    ("Titanium", "Titanium")
)# Unrated < Plus < Bronze < Gold < Platinum < Titanium

form_factors = (
    ("ATX", "ATX"),
    ("Micro ATX", "Micro ATX"),
    ("Mini ITX", "Mini ITX"),
    ("Thin Mini ITX", "Thin Mini ITX"),
    ("EATX", "EATX"),
    ("XL ATX", "XL ATX"),
    ("HPTX", "HPTX"),
    ("SSI CEB", "SSI CEB"),
    ("SSI EEB","SSI EEB")
)


OSModes = (
    (1,"x32bit"),
    (2,"x64bit"),
    (3,"x86bit"),
    (4,"x128bit"),
    (5,"x32bit & x64bit"),
    (6,"x64bit & x86bit")
)

#----------------------------------------------------------------------------------------------------

class Radiator_size(models.Model):
    size = models.CharField(default='0', max_length=10)
    
    def __str__(self):
        return self.size
    

#----------------------------------------------------------------------------------------------------

class Form_Factor(models.Model):
    name = models.CharField(default="", max_length=50)
    
    def __str__(self):
        return self.name
    

#----------------------------------------------------------------------------------------------------

class motherBoard_Socket(models.Model):
    name = models.CharField(default="", max_length=50)
    
    def __str__(self):
        return self.name
    
#----------------------------------------------------------------------------------------------------

class Memory_Frequencies(models.Model):
    value = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.value} Hz"
    
#----------------------------------------------------------------------------------------------------

class PartManager(InheritanceManager):
    def get_compatible(self,price=None,parts = None,additional_conditions = None):
        if not price and not parts:
            return self.all()
        
        conditions = []
        conditions.append(Q(price__lte=price))
        if additional_conditions:
            conditions.extend(additional_conditions)
        part_class = self.model.__name__.lower()
        if not parts or not isinstance(parts,dict):
            return self.filter(*conditions)
        try:
            if part_class=="case":
                if "motherboard" in parts:
                    if len(parts['motherboard'])>0:
                        conditions.append(Q(form_factor_support = parts["motherboard"][0].form_Factor))
                if "casefan" in parts:  
                    fans_with_size={'120':0,'140':0}
                    for fan in parts["casefan"]:
                        fans_with_size[str(fan.size)]+=1
                        if str(fan.size)=='140':
                            fans_with_size["120"]+=1
                    conditions.append(Q(fan_120mm_support__gte=fans_with_size["120"]))
                    conditions.append(Q(fan_140mm_support__gte=fans_with_size["140"]))
                if "cpucooler" in parts:
                    if len(parts['cpucooler'])>0:
                        if parts["cpucooler"][0].type == 'Liquid Cooler':
                            conditions.append(Q(radiator_support = parts["cpucooler"][0].size))
                        else:
                            conditions.append(Q(cpu_cooler_clearance__gte=parts["cpucooler"][0].size))
                if "internalharddrive" in parts:
                    IHD_with_size=[0,0]#3.5,2.5
                    for hard_drive in parts["internalharddrive"]:
                        if hard_drive.type == "HDD SATA" or hard_drive.type == "HDD SAS":
                            IHD_with_size[0]+=1
                        else:
                            IHD_with_size[1]+=1
                    conditions.append(Q(socket3_5__gte=IHD_with_size[0]))
                    conditions.append(Q(socket2_5__gte=IHD_with_size[1]))
                if "opticaldrive" in parts:
                    if len(parts['opticaldrive'])>0:
                        conditions.append(Q(socket5_25__gte=len(parts["opticaldrive"])))
                if "powersupply" in parts:
                    if len(parts["powersupply"])>0:
                        conditions.append(Q(psu="Not Included"))
                        conditions.append(Q(type__in=case_types[parts["powersupply"][0].type]))
                if "videocard" in parts:
                    max_length_video_card = 0
                    for gpu in parts["videocard"]:
                        if gpu.length > max_length_video_card:
                            max_length_video_card=gpu.length
                        conditions.append(Q(gpu_clearance__gte=max_length_video_card))    
            elif part_class=="casefan":
                if "case" in parts:
                    if len(parts["case"])>0:
                        if parts["case"][0].fan_140mm_support <1:
                            conditions.append(~Q(size=140))
            elif part_class=="cpucooler":
                if "case" in parts:
                    if len(parts["case"])>0:    
                        case_con_1 = Q(size__in = parts['case'][0].radiator_support.all())
                        case_con_2 = Q(cooler_height__lte = parts['case'][0].cpu_cooler_clearance)
                        liquid_con = Q(type='Liquid Cooler')
                        conditions.append(Q((case_con_1 & liquid_con) | (case_con_2 & ~liquid_con)))
                if "motherboard" in parts:
                    if len(parts["motherboard"])>0:
                        conditions.append(Q(compatibility=parts["motherboard"][0].socket))
                        if not parts["motherboard"][0].aio_support:
                            conditions.append(~Q(type='Liquid Cooler'))
                elif "cpu" in parts:
                    if len(parts["cpu"])>0:
                        conditions.append(Q(compatibility=parts["cpu"][0].socket))
            elif part_class=="cpu":
                if "motherboard" in parts:
                    if len(parts["motherboard"])>0:
                        conditions.append(Q(socket=parts["motherboard"][0].socket))
            elif part_class=="internalharddrive":
                if 'motherboard' in parts:
                    if len(parts["motherboard"])>0:
                        if parts["motherboard"][0].m2_slot <= 0:
                            conditions.append(~Q(type ='SSD M.2'))
            elif part_class=="memory":
                if "motherboard" in parts:
                    if len(parts["motherboard"])>0:
                        conditions.append(Q(total_capacity__lte=parts["motherboard"][0].max_capacity_per_slot))
                        conditions.append(Q(generation=parts["motherboard"][0].supported_ddr_version))
                if "cpu" in parts:
                    if len(parts["cpu"])>0:
                        conditions.append(Q(total_capacity__lte=parts["cpu"][0].max_memory_support))
                if "memory" in parts:
                    if len(parts["memory"])>0:
                        if "motherboard" in parts:
                            limit_unic = 4 if parts["motherboard"][0].memory_channels=="Quad Channel" else 2 if parts["motherboard"][0].memory_channels=="Dual Channel" else 1  
                            limit_num = parts["motherboard"][0].memory_Slots
                            if len(parts["memory"])>=limit_num:
                                return self.none()
                            if limit_unic!=1:    
                                if len(parts["motherboard"])>0:        
                                    memory_sorter = {}
                                    limit_unic = 4 if parts["motherboard"][0].memory_channels=="Quad Channel" else 2 if parts["motherboard"][0].memory_channels=="Dual Channel" else 1  
                                    limit_num = parts["motherboard"][0].memory_Slots
                                    for ram in parts["memory"]:
                                        if not str(ram.id) in memory_sorter:
                                            memory_sorter[str(ram.id)]=1
                                        else:
                                            memory_sorter[str(ram.id)]+=1
                                    if len(parts["memory"]) > limit_num/limit_unic or len(memory_sorter)>=limit_num/limit_unic:
                                        valid_ids = []
                                        for key in memory_sorter.keys():
                                            if memory_sorter[key]%2!=0:
                                                valid_ids.append(int(key))
                                        conditions.append(Q(id__in=valid_ids))
                                
            elif part_class=="motherboard":
                pcie_count = 0
                if "case" in parts:
                    if len(parts["case"])>0:
                        conditions.append(Q(form_Factor__in=parts["case"][0].form_factor_support.all()))
                is_socket_selected = False
                if "cpu" in parts:
                    if len(parts["cpu"])>0:
                        conditions.append(Q(socket=parts["cpu"][0].socket))
                        is_socket_selected = True
                elif "videocard" in parts:
                    if len(parts["videocard"])>0:
                        pcie_count+=len(parts["videocard"])
                        supported_socket = parts["videocard"][0].compatible_motherboard.all()
                        for gpu in parts["videocard"]:
                            supported_socket = [item1 for item1 in supported_socket if item1 in gpu.compatible_motherboard.all()]
                        conditions.append(Q(socket__in=supported_socket))
                        is_socket_selected=True
                if "memory" in parts:
                    if len(parts["memory"])>0:
                        total_capacity = 0
                        max_capacity = 0
                        memory_sorter = {}
                        ddr_ver = parts["memory"][0].generation
                        is_the_same_ddr_ver = True
                        for ram in parts["memory"]:
                            total_capacity+=ram.total_capacity
                            max_capacity = ram.total_capacity if ram.total_capacity > max_capacity else max_capacity
                            if str(ram.id) in memory_sorter:
                                memory_sorter[str(ram.id)]+=1
                            else:
                                memory_sorter[str(ram.id)]=1
                            is_the_same_ddr_ver = (ddr_ver==ram.generation)
                            
                        if not is_the_same_ddr_ver:
                            return self.none()
                        #conditions.append()
                        conditions.append(Q(supported_ddr_version=ddr_ver))
                        conditions.append(Q(max_Memory__gte=total_capacity))
                        conditions.append(Q(max_capacity_per_slot__gte=max_capacity))
                        daul_num = 0
                        quad_num = 0
                        for key in memory_sorter.keys():
                            daul_num +=memory_sorter[key]/2 + 1 if memory_sorter[key]%2 > 0 else memory_sorter[key]/2
                            quad_num +=memory_sorter[key]/4 + 1 if memory_sorter[key]%4 > 0 else memory_sorter[key]/4  
                        
                        single_channel_cond = Q(Q(memory_channels="Single Channel") & Q(memory_Slots__gte=len(parts["memory"])))
                        daul_channel_cond = Q(Q(memory_channels="Dual Channel") & Q(memory_Slots__gte=daul_num*2))
                        quad_channel_cond = Q(Q(memory_channels="Quad Channel") & Q(memory_Slots__gte=daul_num*4))
                        conditions.append(Q(single_channel_cond | daul_channel_cond | quad_channel_cond))                     
                if "cpucooler" in parts:
                    if len(parts["cpucooler"])>0:
                        if parts["cpucooler"][0].type=='Liquid Cooler':
                            conditions.append(Q(aio_support=True))
                            if not is_socket_selected:
                                conditions.append(Q(socket=parts["cpucooler"][0].compatibility))
                if "internalharddrive" in parts:
                    hard_types = [0,0]#sata,m2
                    for hard in parts["internalharddrive"]:
                        if hard.type in ["SSD M.2","SSD U.2"]:
                            hard_types[1]+=1
                        elif hard.type=="SSD NVMe":
                            pcie_count+=1
                        else:
                            hard_types[0]+=1
                    conditions.append(Q(sata_ports__gte=hard_types[0]))            
                    conditions.append(Q(m2_slot__gte=hard_types[1]))
                if "soundcard" in parts:
                    pcie_count+=len(parts["soundcard"])
                if "wiresnetworkcard" in parts:
                    pcie_count+=len(parts["wiresnetworkcard"])
                if "wirelessnetworkcard" in parts:
                    pcie_count+=len(parts["wirelessnetworkcard"])
                conditions.append(Q(pcie_slots__gte=pcie_count))  
            elif part_class=="opticaldrive":
                if "case" in parts:
                    if len(parts["case"])>0:
                        if parts["case"][0].socket5_25<1:
                            return self.none()
            elif part_class=="videocard":
                if "case" in parts:
                    if len(parts["case"])>0:
                        conditions.append(Q(length__lte=parts["case"][0].gpu_clearance))
                if "motherboard" in parts:
                    if len(parts["motherboard"])>0:
                        conditions.append(Q(compatible_motherboard=parts["motherboard"][0].socket))  
            elif part_class=="powersupply":
                if "case" in parts:
                    if len(parts["case"])>0:
                        if parts["case"][0].psu != 'Not Included':
                            return self.none()
                total_wattage = 0
                for part_categroy in parts.values():
                    for part in part_categroy:
                        total_wattage+=part.power_requirement
                print(total_wattage)
                total_wattage*=1.25
                conditions.append(Q(wattage__gte=total_wattage))
                if 'videocard' in parts:
                    if len(parts['videocard'])>1:
                        conditions.append(Q(multi_gpu_support=True))
                if 'case' in parts:
                    if len(parts["case"])>0:
                        psutype = 'SFX'
                        if parts['case'][0].type in power_supply_and_cases['ATX']:
                            psutype = 'ATX'
                    conditions.append(Q(type = psutype))
                 
        
            return self.filter(*conditions)
        except Exception as Ex:
            print(f"Error: {Ex}")
            return self.none()
#----------------------------------------------------------------------------------------------------

class Part(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=200)
    price = models.FloatField()
    population = models.IntegerField(default=0)#increase in every order by one
    like_count = models.PositiveBigIntegerField(default=0)
    in_storage = models.PositiveIntegerField(default=0)
    #Rate = models.DecimalField(max_digits=3, decimal_places=2)
    #image
    image_filename = models.ImageField(upload_to=imageSaver,null=True,blank=True)
    content_type = models.ForeignKey(ContentType,null=True, on_delete=models.CASCADE, editable=False)
    date_created = models.DateField(auto_now=True)
    power_requirement = models.FloatField(default=0.0)
    objects = PartManager()

    
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        if not self.content_type:
            self.content_type = ContentType.objects.get_for_model(self)
        super().save(*args, **kwargs)
#----------------------------------------------------------------------------------------------------

class Case(Part):
    #general
#    category = models.CharField(default="Case",choices=(("Case","Case")), max_length=10)
    type = models.CharField(default="ATX Mid Tower" , choices=case_types , max_length=100)
    color = models.CharField(default="Black", max_length=50)
    side_panel = models.CharField(default="normal", max_length=50)
    #power
    psu = models.CharField(default="Not Included", max_length=50)
    #motherBoard
    form_factor_support = models.ManyToManyField("Form_Factor")#  Case <---> motherboard
    #cooling
    fan_120mm_support = models.IntegerField(default=0)
    fan_140mm_support = models.IntegerField(default=0)
    cpu_cooler_clearance = models.IntegerField(default=0)#  Case <---> cpu cooler
    radiator_support = models.ManyToManyField("Radiator_size",null=True,blank=True)# water-c type:120mm , 240mm , 280mm , 360mm , 420mm , +480mm )  
    #Video Card
    gpu_clearance = models.IntegerField(default=0)#  Case <---> video card
    #Storage
    socket5_25 = models.IntegerField(default=0)
    #فتحات التخزين الخارجية (مثل محركات الأقراص CD\DVD)
    socket3_5 = models.IntegerField(default=0)
    #الخانات الداخلية لتركيب الأقراص الصلبة
    socket2_5 = models.IntegerField(default=0)
    #مخصصة لأاقراص معينة ك ssd
    

    def __str__(self):
   
        return self.name


    
#----------------------------------------------------------------------------------------------------

class CaseAccessory(Part):
    
    #general
#    category = models.CharField(default="Case Accessory",choices=(("Case Accessory","Case Accessory")), max_length=10)
    type = models.CharField(default="", max_length=80)
    features = models.TextField(default="")
    #case
    compatibility = models.CharField(default="None", max_length=50)
    form_factor = models.CharField(default="5.25", choices=Form_Factor_in_Case , max_length=50)
    

    def __str__(self):
   
        return self.name

#----------------------------------------------------------------------------------------------------

class CaseFan(Part):
#    category = models.CharField(default="Case Fan",choices=(("Case Fan","Case Fan")), max_length=10)
    size = models.IntegerField(choices=Fan_Size)
    color = models.CharField(default="No Color", max_length=50,null=True,blank=True)
    fan_type = models.CharField(default="Standard" , choices=Fan_Type , max_length=50)# Standard , Static Pressure , High Airflow , Silent , RGB/ARGB , Slim , Industrial
    compatibility = models.CharField(default="", max_length=100)
    features = models.TextField(default="")
    #statues info
    Lrpm = models.IntegerField(default=0,null=True,blank=True)
    Urpm = models.IntegerField(default=0,null=True,blank=True)
    pwm = models.BooleanField(default=False)
    Lairflow = models.FloatField(default=0,null=True,blank=True)
    Uairflow = models.FloatField(default=0,null=True,blank=True)
    Lnoise_level = models.FloatField(default=0,null=True,blank=True)
    Unoise_level = models.FloatField(default=0,null=True,blank=True)
    rgb_support = models.BooleanField(default=False)
    
    
    def __str__(self):
   
        return self.name

#----------------------------------------------------------------------------------------------------

class CpuCooler(Part):

    #general
#    category = models.CharField(default="CPU Cooler",choices=(("CPU Cooler","CPU Cooler")), max_length=10)
    color = models.CharField(default="No Color", max_length=50,null=True,blank=True)
    size = models.IntegerField(choices=Fan_Size)
    type = models.CharField(default="Air Cooler", choices=Cpu_Fan_Type , max_length=50)# Air Cooler , Liquid Cooler , Passive  Cooler , Hybrid Cooler , Sub-Ambient Cooler
    compatibility = models.ManyToManyField("motherBoard_Socket")
    cooler_height = models.FloatField(default=0)
    features = models.TextField(default="")
    #statues info
    Lrpm = models.IntegerField(default=0,null=True,blank=True)
    Urpm = models.IntegerField(default=0,null=True,blank=True)
    Lnoise_level = models.FloatField(default=0,null=True,blank=True)
    Unoise_level = models.FloatField(default=0,null=True,blank=True)
    

    def __str__(self):
   
        return self.name

#----------------------------------------------------------------------------------------------------

class Cpu(Part):

    #general
#    category = models.CharField(default="CPU",choices=(("CPU","CPU")), max_length=10)
    release_year = models.IntegerField(default=0)
    #socket
    socket = models.ForeignKey("motherBoard_Socket", on_delete=models.CASCADE)# cpu <---> motherboard
    #core
    core_count = models.IntegerField(default=0)
    core_clock = models.DecimalField( max_digits=4, decimal_places=2)
    boost_clock = models.DecimalField( max_digits=4, decimal_places=2)
    #Memory
    max_memory_support = models.IntegerField(default=2)
    #cooling
    cooling_included = models.BooleanField()
    #graphic
    graphics = models.CharField(max_length=100,null=True,blank=True)
    integrated_graphics = models.BooleanField()
    #Simultaneous Multithreading
    smt = models.BooleanField()
    

    def __str__(self):
   
        return self.name

#----------------------------------------------------------------------------------------------------

class ExternalHardDrive(Part):
    
    #general
#    category = models.CharField(default="External Hard Drive",choices=(("External Hard Drive","External Hard Drive")), max_length=10)
    pricePerGB = models.DecimalField(max_digits=6, decimal_places=5)
    features = models.TextField(default="")
    color = models.CharField(default="no color", max_length=50)
    #statues
    type = models.CharField(default="Desktop" , choices=ExternalHardDrive_type , max_length=50)
    interface = models.CharField(default='',max_length=150)
    capacity = models.IntegerField(default=0)
    #speed
    max_speed = models.CharField(default="", max_length=50)
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class FanController(Part):
    
    #general
#    category = models.CharField(default="Case",choices=(("Fan Controller","Fan Controller")), max_length=10)
    features = models.TextField(default="")
    compatibility = models.CharField(default="", max_length=50)
    color = models.CharField(default="no color", max_length=50)
    #channels
    channels = models.IntegerField(default=0)
    channelsWattage = models.IntegerField(default=0)
    #round controller
    pwm = models.BooleanField(default=0)
    #power
    max_power = models.IntegerField(default=0)
    #usage
    formFactor = models.CharField(default="5.25", choices=Form_Factor_in_Case , max_length=50)#5.25 , 3.5 , 2.5   
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class headphones(Part):
#    category = models.CharField(default="Headphones",choices=(("Headphones","Headphones")), max_length=10)
    type = models.CharField(choices=headphones_Type , default="Circumaural" , max_length=50)## Circumaural , Supra-Aural , Earbud , In Ear 
    LfrequencyResponse = models.IntegerField(default=0)
    UfrequencyResponse = models.IntegerField(default=0)
    microphone = models.BooleanField()
    wireless = models.BooleanField()
    enclosureType = models.CharField(default="Open" , choices=headphones_enclosureType , max_length=50)
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    
    
    def __str__(self):
        return self.name


#----------------------------------------------------------------------------------------------------

class InternalHardDrive(Part):
#    category = models.CharField(default="Internal Hard Drive",choices=(("Internal Hard Drive","Internal Hard Drive")), max_length=10)
    type = models.CharField(default="HDD SATA", choices=InternalHardDrive_type , max_length=50)
    interface = models.CharField(default='',max_length=150)
    capacity = models.IntegerField(default=0)
    pricePerGB = models.DecimalField(max_digits=6, decimal_places=5)
    cache = models.IntegerField(default=0)
    formFactor = models.CharField(default="",max_length=50)
    features = models.TextField(default="")
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class Keyboard(Part):
#    category = models.CharField(default="Keyboard",choices=(("Keyboard","Keyboard")), max_length=10)
    style = models.CharField(default="", max_length=50)
    switches = models.CharField(default="", max_length=50)
    backlit = models.CharField(default="no Back-Light", max_length=50)
    tenkeyless = models.BooleanField()
    connectionType = models.CharField(default="Wired", max_length=50)
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    

    def __str__(self):
        return self.name


#----------------------------------------------------------------------------------------------------

class Memory(Part):
    
    #general
#    category = models.CharField(default="Memory",choices=(("Memory","Memory")), max_length=10)
    generation = models.CharField(default='DDR3',choices=ddr_versions, max_length=10)
    speed = models.ForeignKey("Memory_Frequencies", on_delete=models.CASCADE)
    pricePerGB = models.DecimalField(max_digits=7, decimal_places=5)
    color = models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    #modules and capacity
    unit_number = models.IntegerField(default=0)
    unit_capacity = models.IntegerField(default=0)
    total_capacity = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------


class Monitor(Part):
    

    #Desplay info
#    category = models.CharField(default="Monitor",choices=(("Monitor","Monitor")), max_length=10)
    screenSize = models.DecimalField(max_digits=4, decimal_places=2)
    resolution = models.CharField(default="1366x768" , choices=resolutions , max_length=50)##
    refreshRate = models.IntegerField(default=0)
    responseTime = models.IntegerField(null=True,blank=True)
    aspectRatio = models.CharField(default="", max_length=50)##
    #more info
    panelType = models.CharField(default="", max_length=50)##
    features = models.TextField(default="")
    
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class MotherBoard(Part):
    
    #main attribute
#    category = models.CharField(default="MotherBoard",choices=(("MotherBoard","MotherBoard")), max_length=10)
    color = models.CharField(default="no color", max_length=50)
    additional_features = models.TextField(default="")
    #CPU socket
    socket = models.ForeignKey("motherBoard_Socket", on_delete=models.CASCADE)#  motherboard <---> cpu
    
    cpu_compatibility = models.CharField(default="", max_length=50)
    #size and form
    form_Factor = models.ForeignKey("Form_Factor", on_delete=models.DO_NOTHING)#  motherboard <---> case


 
    #Memory
    max_Memory = models.IntegerField(default=0)
    memory_Slots = models.SmallIntegerField(default=0)
    supported_ddr_version = models.CharField(default="DDR4" , choices=ddr_versions , max_length=10)
    supported_memory_frequencies = models.ManyToManyField("Memory_Frequencies")
    Extreme_Memory_Profile_support = models.BooleanField()
    memory_channels = models.CharField(default="Single Channel" , choices=memory_channels_list , max_length=50)
    max_capacity_per_slot = models.IntegerField(default=0)
    #storage
    m2_slot = models.IntegerField(default=0)
    sata_ports = models.IntegerField(default=0)
    #USBs
    usb_2 = models.SmallIntegerField(default=0)
    usb_3 = models.SmallIntegerField(default=0)
    usb_C = models.SmallIntegerField(default=0)
    #network
    Lan_network = models.CharField(default="", max_length=50)
    wifi_network = models.CharField(default="", max_length=50)
    #audio
    audio_chipset = models.CharField(default="", max_length=50)
    #power
    power_phases = models.SmallIntegerField(default=0)
    #cooling_support
    fan_headers = models.SmallIntegerField(default=0)
    aio_support = models.BooleanField()
    #extansion_capabilities
    pcie_slots = models.SmallIntegerField(default=0)
    #extra
    rgb_support = models.BooleanField()
    release_year = models.SmallIntegerField(default=0)
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class Mouse(Part):
    
#    category = models.CharField(default="Mouse",choices=(("Mouse","Mouse")), max_length=10)
    tracking_method = models.CharField(default="Optical" , choices=mouse_tracking_methods , max_length=50)##Touchpad , Optical , Laser , Trackball
    max_dpi = models.IntegerField(default=0)
    hand_orientation = models.CharField(default="Right" , choices=mouse_hand_orientation , max_length=50)##Both , Right , Left
    connectionType = models.CharField(default="Wired" , choices=connection_types , max_length=50)##Wired , Wireless , Bluetooth Wireless
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class OpticalDrive(Part):
    
    #general
#    category = models.CharField(default="Optical Drive",choices=(("Optical Drive","Optical Drive")), max_length=10)
    features = models.TextField(default="")
    #blu-ray
    blu_ray_read_speed = models.IntegerField(default=0,null=True,blank=True)
    blu_ray_write_speed = models.CharField(default="", max_length=50,null=True,blank=True)# BD-R / BD-R DL / BD-RE / BD-RE DL
    #dvd
    dvd_read_speed = models.IntegerField(default=0,null=True,blank=True)
    dvd_write_speed = models.CharField(default="", max_length=50,null=True,blank=True)# DVD-R / DVD-RW / DVD+RW / DVD+R / DVD-R DL / DVD+R DL / DVD-RAM
    #cd
    cd_read_speed = models.IntegerField(default=0,null=True,blank=True)
    cd_write_speed = models.CharField(default="", max_length=50,null=True,blank=True)# CD-R / CD-RW


    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class PowerSupply(Part):
    
#    category = models.CharField(default="Power Supply",choices=(("Power Supply","Power Supply")), max_length=10)
    type = models.CharField(default="ATX" , choices=(("ATX","ATX"),("SFX","SFX")) , max_length=50)
    efficiency = models.CharField(default="Plus", choices=power_supply_efficiency , max_length=50)# Plus < Bronze < Gold < Platinum < Titanium
    wattage = models.IntegerField(default=0)
    modular = models.CharField(default="False" , choices=power_supply_Modular , max_length=50)
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    dimensions = models.CharField(default="unknown", max_length=50)
    #connectors
    ATX_24pin_connectors = models.IntegerField(default=0)
    EPS_8pin_connectors = models.IntegerField(default=0)
    PCIe_6_Pls_2pin_connectors = models.IntegerField(default=0)
    SATA_connectors = models.IntegerField(default=0)
    Molex_connectors = models.IntegerField(default=0)
    #multi GBU
    multi_gpu_support = models.BooleanField()
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------
 
class SoundCard(Part):
     
#    category = models.CharField(default="Sound Card",choices=(("Sound Card","Sound Card")), max_length=10)
    channels = models.FloatField()
    digital_audio = models.IntegerField(null=True,blank=True)
    snr = models.IntegerField(default=0,null=True,blank=True)
    sample_rate = models.IntegerField(default=0,null=True,blank=True)
    chipset = models.CharField(default="", max_length=50)
    interface = models.CharField(default="PCIe x1" , choices=Extention_Cards_interface , max_length=50)##
    features = models.TextField(default="")
    
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class Speakers(Part):
    
#    category = models.CharField(default="Speakers",choices=(("Speakers","Speakers")), max_length=10)
    color =  models.CharField(default="no color", max_length=50)
    configuration = models.FloatField()
    wattage = models.IntegerField(default=0)
    Lfrequency_response = models.IntegerField(default=0,null=True,blank=True)
    Ufrequency_response = models.IntegerField(default=0,null=True,blank=True)
    features = models.TextField(default="")
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------

class ThermalPaste(Part):
#    category = models.CharField(default="Thermal Paste",choices=(("Thermal Paste","Thermal Paste")), max_length=10)
    amountInOne = models.FloatField()
    features = models.TextField(default="")
    
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------


class VideoCard(Part):

#    category = models.CharField(default="Case",choices=(("Case","Case")), max_length=10)
    chipset = models.CharField(default="", max_length=100)
    GRAM = models.IntegerField(default=0)
    coreClock = models.FloatField(default=0,null=True,blank=True)
    boostClock = models.FloatField(default=0,null=True,blank=True)
    color =  models.CharField(default="no color", max_length=50)
    length = models.IntegerField(default=0)
    compatible_motherboard = models.ManyToManyField("motherBoard_Socket")
    interface = models.CharField(default="PCIe 4.0", choices=Extention_Cards_interface , max_length=50)# PCI , PCIe 1.0  , PCIe 4.0 , PCIe 8.0 , PCIe 16.0
    release_year = models.IntegerField(default=0,null=True,blank=True)
    
    
    def __str__(self):
        return self.name
   
#----------------------------------------------------------------------------------------------------

class Webcam(Part):
    
#    category = models.CharField(default="Case",choices=(("Case","Case")), max_length=10)
    resolutions = models.CharField(default="360P" , choices=cam_Resolutions , max_length=10)
    connection = models.CharField(default="", max_length=50)
    focus_type = models.CharField(default="Manual" , choices=focus_types , max_length=10)#Manual , Auto , Fixed
    os  = models.CharField(default="", max_length=50)
    fov = models.FloatField()
    features = models.TextField(default="")
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------


class WiresNetworkCard(Part):
    
#    category = models.CharField(default="Case",choices=(("Case","Case")), max_length=10)
    interface = models.CharField(default="PCIe x1" , max_length=20)
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------


class WirelessNetworkCard(Part):
    
#    category = models.CharField(default="Case",choices=(("Case","Case")), max_length=10)
    protocol = models.CharField(default="",max_length=50)
    interface = models.CharField(default="PCIe x1" , max_length=20)
    color =  models.CharField(default="no color", max_length=50)
    features = models.TextField(default="")
    

    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------
    '''
    motherboard sockets:
    
2 x G34
2 x LGA1366
2 x LGA2011
2 x LGA2011-3
2 x LGA2011-3 Narrow
AM1
AM2
AM2+/AM2
AM3
AM3+
AM3+/AM3
AM3/AM2+
AM3/AM2+/AM2
AM4
AM5
FM1
FM2
FM2+
Integrated A4-5000
Integrated Athlon II X2 215
Integrated Atom (بأنواع متعددة مثل D2500 وD2550...)
Integrated C-Series (مثل C-70)
Integrated Celeron (مثل 1037U، J1900...)
Integrated E-Series (مثل E-350، E-450)
Integrated Pentium (مثل J3710، N3700)
Integrated Xeon (مثل D-1520، D-1541...)
LGA1150
LGA1151
LGA1155
LGA1156
LGA1200
LGA1366
LGA1700
LGA2011
LGA2011-3
LGA2011-3 Narrow
LGA2066
LGA775
sTR4
sTRX4
    '''
    
    
#form factors    
'''
    ATX
    Micro ATX
    Mini ITX
    Thin Mini ITX
    Mini DTX
    Flex ATX
    EATX
    XL ATX
    HPTX
    SSI CEB
    SSI EEB
    '''

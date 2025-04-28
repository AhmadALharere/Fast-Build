
from django.http import JsonResponse
from rest_framework import generics
from .models import Case,CaseFan ,motherBoard_Socket, CaseAccessory, Cpu, CpuCooler, ExternalHardDrive, Radiator_size , FanController, Form_Factor, headphones, InternalHardDrive, Keyboard, Memory, Monitor, Mouse, MotherBoard, OpticalDrive,  PowerSupply, SoundCard, Speakers,ThermalPaste , VideoCard ,Webcam, WirelessNetworkCard,WiresNetworkCard 
import json
from .serializer import CeseSerializer,CaseAccessorySerializer,CeseFanSerializer,CpuCoolerSerializer,CpuSerializer,VideoCardSerializer,MouseSerializer,ExternalHardDriveSerializer,FanControllerSerializer,headphonesSerializer,InternalHardDriveSerializer,KeyboardSerializer,MemorySerializer,MonitorSerializer,MotherBoardSerializer,OpticalDriveSerializer,PowerSupplySerializer,SoundCardSerializer,SpeakersSerializer,WiresNetworkCardSerializer,WirelessNetworkCardSerializer,WebcamSerializer,ThermalPasteSerializer,serializers



def load_Cases(request):
    
    #if request.method == 'POST':
        
        for case in Case.objects.all():
                case.delete()
        
        
        json_file = open("PcPart/data/Parts/case.json","r")
        data = json.load(json_file)
        
        
        for item in data:
            
                serializer = CeseSerializer(data=item)
                if serializer.is_valid():
                    case = serializer.save()
                else:
                    return JsonResponse(f"field in{item['name']}",safe=False)
            
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Case_accessorys(request):
    
    #if request.method == 'POST':
        for caseacc in CaseAccessory.objects.all():
                caseacc.delete()
        
        
        json_file = open("PcPart/data/Parts/case_accessory.json","r")
        data = json.load(json_file)
        
        
        for item in data:
            
            
            
                serializer = CaseAccessorySerializer(data=item)
                if serializer.is_valid():
                    caseAccessory = serializer.save()
                else:
                    return JsonResponse(f"field in{item['name']}",safe=False)
            
        return JsonResponse("success!!",safe=False)
            

def load_Case_Fans(request):
    
    #if request.method == 'POST':
        
        for casefan in CaseFan.objects.all():
                casefan.delete()
        
        
        json_file = open("PcPart/data/Parts/case_fan.json","r")
        data = json.load(json_file)
        
        
        for item in data:
            
        
                serializer = CeseFanSerializer(data=item)
                if serializer.is_valid():
                    casefan = serializer.save()
                else:
                    return JsonResponse(f"field in{item['name']}",safe=False)
            
        return JsonResponse("success!!",safe=False)
            

def load_Cpu_Cooler(request):

  
    #if request.method == 'POST':
        
        for cpucooler in CpuCooler.objects.all():
                cpucooler.delete()
        
        
        
        json_file = open("PcPart/data/Parts/cpu_cooler.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            cpufan = CpuCooler.objects.create(
                                        
                                        name = item['name'],
                                        price = item['price'] if item['price']!=None else 0,
                                        color = item['color'],
                                        size = item['size'],
                                        type = item['type'],# Air Cooler , Liquid Cooler , Passive  Cooler , Hybrid Cooler , Sub-Ambient Cooler
                                        compatibility = item['compatibility'] if item['compatibility']!=None else "",
                                        cooler_height = item['cooler_height'],
                                        features = item['features'] if item['features']!=None else "",
                                        population = 0,#increase in every order by one
                                        in_storage = 0,
                                        #statues info
                                        Lrpm = item['Lrpm'],
                                        Urpm = item['Urpm'],
                                        Lnoise_level = item['Lnoise_level'],
                                        Unoise_level = item['Unoise_level']
                                      )
            
            #return JsonResponse("success!!",safe=False)
            
            
            '''
            print(item.__str__())    
            i+=1     
                
            serializer = CpuCoolerSerializer(data=item)
            if serializer.is_valid():
                cpucooler = serializer.save()
            else:
                return JsonResponse(f"field in id: {i}  name: {item['name']}",safe=False)
            '''
        return JsonResponse("success!!",safe=False)
            

def load_Cpus(request):
    
    #if request.method == 'POST':
        for cpu in Cpu.objects.all():
                cpu.delete()
        
        
        
        json_file = open("PcPart/data/Parts/cpu.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:
                cpu = Cpu.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                release_year = item['release_year'],
                socket = motherBoard_Socket.objects.get(name=item['socket']),
                core_count = item['core_count'],
                core_clock = item['core_clock'],
                boost_clock = item['boost_clock'],
                tdp = item['tdp'],
                max_memory_support = item['max_memory_support'],
                cooling_included = item['cooling_included'],
                graphics = item['graphics'],
                integrated_graphics = item['integrated_graphics'],
                smt = item['smt'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_External_Hard_Drive(request):
    
    #if request.method == 'POST':
        
        for EHD in ExternalHardDrive.objects.all():
                EHD.delete()
        
        
        
        json_file = open("PcPart/data/Parts/external_hard_drive.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:
                ehd = ExternalHardDrive.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                pricePerGB = item['price_per_gb'] if item['price_per_gb']!=None else 0,
                features = item['features'] if item['features']!=None else "",
                color = item['color'] if item['color']!=None else "Unknown",
                type = item['type'],
                interface = item['interface'],
                capacity = item['capacity'],
                max_speed = item['max_speed'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Internal_Hard_Drive(request):
    
    #if request.method == 'POST':
        
        for IHD in InternalHardDrive.objects.all():
                IHD.delete()
        
        
        
        json_file = open("PcPart/data/Parts/internal_hard_drive.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                ihd = InternalHardDrive.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                pricePerGB = item['price_per_gb'] if item['price_per_gb']!=None else 0,
                features = Ffeatures,
                type = item['type'],
                interface = item['interface'],
                capacity = item['capacity'],
                cache = item['cache'],
                formFactor = item['form_factor'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Fan_Controller(request):
    
    #if request.method == 'POST':
        
        for FC in FanController.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/fan_controller.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Fc = FanController.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                features = item['features'],
                compatibility = item['compatibility'],
                color = item['color'],
                channels = item['channels'],
                channelsWattage = item['channel_wattage'],
                pwm = item['pwm'],
                max_power = item['max_power'],
                formFactor = item['form_factor'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Headphones(request):
    
    #if request.method == 'POST':
        
        for FC in headphones.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/headphones.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                
                Fr = item['frequency_response']
                
                headphone = headphones.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                type = item['type'],
                features = Ffeatures,
                LfrequencyResponse = Fr[0],
                UfrequencyResponse = Fr[1],
                color = item['color'],
                microphone = item['microphone'],
                wireless = item['wireless'],
                enclosureType = item['enclosure_type'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Keyboard(request):
    
    #if request.method == 'POST':
        
        
        for FC in Keyboard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/keyboard.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                
                
                keyboard = Keyboard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                style = item['style'],
                features = Ffeatures,
                switches = item['switches'],
                backlit = item['backlit'],
                color = item['color'],
                tenkeyless = item['tenkeyless'],
                connectionType = item['connection_type'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Memory(request):
    
    #if request.method == 'POST':
        
        for FC in Memory.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/memory.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                GandS = item['speed']
                modules = item['modules']
                
                
                memory = Memory.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                generation = GandS[0],
                speed = GandS[1],
                features = Ffeatures,
                pricePerGB = item['price_per_gb'],
                color = item['color'],
                unit_number = modules[0],
                unit_capacity = modules[1],
                total_capacity = item['total_capacity'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def find_socket(socket):
    if socket.find("Integrated")==-1: 
        return socket 
    elif socket.find("Integrated Atom")!=-1:
        return "Integrated Atom"
    elif socket.find("Integrated Celeron")!=-1:
        return "Integrated Celeron"
    elif socket.find("Integrated Pentium")!=-1:
        return "Integrated Pentium"
    elif socket.find("Integrated Xeon")!=-1:
        return "Integrated Xeon"
    elif socket.find("Integrated E")!=-1:
        return "Integrated E-Series"
    elif socket.find("Integrated C")!=-1:
        return "Integrated C-Series"
    else:
        return socket


def load_MotherBoard(request):
    
    #if request.method == 'POST':
        
        for FC in MotherBoard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/motherBoard.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                print(item['socket'])
                soc = motherBoard_Socket.objects.get(name=find_socket(item['socket']))
                Ff = Form_Factor.objects.get(name=item['form_factor'].replace(" ",""))
                usb_ports = item['usb_ports']
                network = item['network']
                cooling_support = item['cooling_support']
                expansion_capabilities = item['expansion_capabilities']
                supported_memory_frequencies = item['supported_memory_frequencies']
                SMFAsStr = ""
                for j,freq in enumerate (supported_memory_frequencies):
                    SMFAsStr += (str)(freq)+(' / ' if j != supported_memory_frequencies.__len__() + 1 else " MHz" )
                
                motherBoard = MotherBoard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                color = item['color'] if item['color']!=None else "Unknown",
                additional_features = item['additional_features'],
                #CPU socket
                socket = soc,
                cpu_compatibility = item['cpu_compatibility'],
                #size and form
                form_Factor = Ff,
                #Memory
                max_Memory = item['max_memory'],
                memory_Slots = item['memory_slots'],
                supported_ddr_version = item['supported_ddr_version'],
                supported_memory_frequencies =SMFAsStr,
                xmp_support = item['xmp_support'],
                memory_channels = item['xmp_support'],
                max_capacity_per_slot = item['max_capacity_per_slot'],
                #storage
                m2_slut = item['m2_slots'],
                sata_ports = item['sata_ports'],
                #USBs
                usb_2 = usb_ports["USB_2.0"],
                usb_3 = usb_ports["USB_3.0"],
                usb_C = usb_ports["USB-C"],
                #network
                Lan_network = network["LAN"],
                wifi_network = network["Wi-Fi"],
                #audio
                audio_chipset = item['audio_chipset'],
                #power
                power_phases = item['power_phases'],
                #cooling_support
                fan_headers = cooling_support['fan_headers'],
                aio_support = cooling_support['aio_support'],
                #expansion_capabilities
                pci_slots = expansion_capabilities["PCI"],
                pcie_x1_slots = expansion_capabilities["PCIe_x1"],
                pcie_x4_slots = expansion_capabilities["PCIe_x4"],
                pcie_x8_slots = expansion_capabilities["PCIe_x8"],
                pcie_x16_slots = expansion_capabilities["PCIe_x16"],
                #extra
                rgb_support = item['rgb_support'] if item['rgb_support']==True|False else False,
                release_year = item['release_year'],
                population = 0,#increase in every order by one
                in_storage = 0
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Monitor(request):
    
    #if request.method == 'POST':
        
        for FC in Monitor.objects.all():
                FC.delete()
        
        
        json_file = open("PcPart/data/Parts/monitor.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                resolutions = item['resolution']
                RAsStr = (str)(resolutions[0])+'x'+(str)(resolutions[1])
                
                monitor = Monitor.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                screenSize = item['screen_size'],
                resolution = RAsStr,
                features = Ffeatures,
                refreshRate = item['refresh_rate'],
                responseTime = item['response_time'],
                panelType = item['panel_type'],
                aspectRatio = item['aspect_ratio'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Mouse(request):
    
    #if request.method == 'POST':
        
        for FC in Mouse.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/mouse.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                
                mouse = Mouse.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                tracking_method = item['tracking_method'],
                max_dpi = item['max_dpi'],
                hand_orientation = item['hand_orientation'],
                connectionType = item['connection_type'],
                color = item['color']if item['color']!=None else "Unknown",
                features = Ffeatures,
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)

def load_OpticalDrive(request):
    
    #if request.method == 'POST':
        
        for FC in OpticalDrive.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/optical_drive.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                
                Od = OpticalDrive.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                features = Ffeatures,
                bd = item['bd'],
                bd_write = item['bd_write'],
                dvd = item['dvd'],
                dvd_write = item['dvd_write'],
                cd = item['cd'],
                cd_write = item['cd_write'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)



def load_PowerSupply(request):
    
    #if request.method == 'POST':
        
        for FC in PowerSupply.objects.all():
                FC.delete()
        
        
        json_file = open("PcPart/data/Parts/power_supply.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                    
                connectors = item['connectors']
                
                Ps = PowerSupply.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                features = Ffeatures,
                type = item['type'],
                efficiency = item['efficiency'],
                wattage = item['wattage'],
                modular = item['modular'],
                color = item['color'] if item['color']!= None else "Unknown",
                dimensions = item['dimensions'],
                ATX_24pin_connectors = connectors['ATX_24pin'],
                EPS_8pin_connectors = connectors['EPS_8pin'],
                PCIe_6_Pls_2pin_connectors = connectors['PCIe_6+2pin'],
                SATA_connectors = connectors['SATA'],
                Molex_connectors = connectors['Molex'],
                multi_gpu_support = item['multi_gpu_support'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_SoundCard(request):
    
    #if request.method == 'POST':
        
        for FC in SoundCard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/sound_card.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                Sc = SoundCard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                features = Ffeatures,
                channels = item['channels'],
                digital_audio = item['digital_audio'],
                snr = item['snr'],
                sample_rate = item['sample_rate'],
                chipset = item['chipset'],
                interface = item['interface'],
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_Speakers(request):
    
    #if request.method == 'POST':
        
        for FC in Speakers.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/speakers.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                frequency_response = item['frequency_response']
                
                
                speakers = Speakers.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                color = item['color'] if item['color']!=None else "Unknown",
                features = Ffeatures,
                configuration = item['configuration'],
                wattage = item['wattage'],
                Lfrequency_response = frequency_response[0] if frequency_response!=None else None,
                Ufrequency_response = frequency_response[1] if frequency_response!=None else None,
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)


def load_ThermalPaste(request):
    
    #if request.method == 'POST':
        
        for FC in ThermalPaste.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/thermal_paste.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                Ffeatures = ""
                
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                thermalPaste = ThermalPaste.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                amountInOne = item['amount'],
                features = Ffeatures,
                population = 0,#increase in every order by one
                in_storage = 0,
                )
                         
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)



def load_VideoCard(request):
    
    #if request.method == 'POST':
        
        for FC in VideoCard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/gpu.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                '''
                serializer = VideoCardSerializer(data=item)
                if serializer.is_valid():
                    videocard = serializer.save()
                else:
                    return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: Serializer validation-------item: {item}",safe=False)
                '''
                
                videocard = VideoCard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                color = item['color']if item['color']!=None else "Unknown",
                chipset = item['chipset'],
                GRAM = item['memory'],
                coreClock = item['core_clock'],
                boostClock = item['boost_clock'],
                length = item['length'] if item['length'] !=None else 240,
                interface = item['interface'],
                power_requirement = item['power_requirement'],
                release_year = item['release_year'],
                population = 0,#increase in every order by one
                in_storage = 0
                )
                
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)



def load_Webcam(request):
    
    #if request.method == 'POST':
        
        for FC in Webcam.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/webcam.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                '''
                serializer = VideoCardSerializer(data=item)
                if serializer.is_valid():
                    videocard = serializer.save()
                else:
                    return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: Serializer validation-------item: {item}",safe=False)
                '''
                res = item['resolutions']
                Ffeatures = ""
                OSs = ""
                
                
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                for statement in item['os']:
                    OSs+=statement+' , '
                
                
                webcam = Webcam.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                resolutions = res[0],
                connection = item['connection'],
                features = Ffeatures,
                focus_type = item['focus_type'],
                os = OSs,
                fov = item['fov'],
                population = 0,#increase in every order by one
                in_storage = 0
                )
                
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)



def load_WiresNetworkCard(request):
    
    #if request.method == 'POST':
        
        for FC in WiresNetworkCard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/wired_network_card.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                '''
                serializer = VideoCardSerializer(data=item)
                if serializer.is_valid():
                    videocard = serializer.save()
                else:
                    return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: Serializer validation-------item: {item}",safe=False)
                '''
                Ffeatures = ""
                
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                
                
                wiresNetworkCard = WiresNetworkCard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                interface = item['interface'],
                color = item['color'] if item['color']!=None else "Unknown",
                features = Ffeatures,
                population = 0,#increase in every order by one
                in_storage = 0
                )
                
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)
    
    
    
def load_WirelessNetworkCard(request):
    
    #if request.method == 'POST':
        
        for FC in WirelessNetworkCard.objects.all():
                FC.delete()
        
        
        
        json_file = open("PcPart/data/Parts/wireless_network_card.json","r")
        data = json.load(json_file)
        
        i=0
        for item in data:
            
            i+=1 
            try:    
                '''
                serializer = VideoCardSerializer(data=item)
                if serializer.is_valid():
                    videocard = serializer.save()
                else:
                    return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: Serializer validation-------item: {item}",safe=False)
                '''
                Ffeatures = ""
                
                
                for statement in item['features']:
                    Ffeatures+=statement+' , '
                
                
                wirelessNetworkCard = WirelessNetworkCard.objects.create(
                
                name = item['name'],
                price = item['price'] if item['price']!=None else 0,
                interface = item['interface'],
                protocol = item['protocol'],
                color = item['color'] if item['color']!=None else "Unknown",
                features = Ffeatures,
                population = 0,#increase in every order by one
                in_storage = 0
                )
                
            except Exception as EX:
                return JsonResponse(f"field in id {i} name: {item['name']}-------Error Code: {EX}-------item: {item}",safe=False)
        return JsonResponse("success!!",safe=False)
            
    #return JsonResponse("something went wrong...",safe=False)



def init_motherBoardSocket(request):
    
    for MBS in motherBoard_Socket.objects.all():
                MBS.delete()
    
    soc = ["AM1","AM2","AM2+","AM3","AM3+","AM2+/AM2","AM3+/AM3","AM3/AM2+","AM3/AM2+/AM2","AM4","AM5","FM1","FM2","FM2+","LGA775","LGA1150","LGA1151","LGA1155","LGA1156","LGA1200","LGA1366","LGA1700","LGA2011","LGA2011-3","LGA2011-3 Narrow","LGA2066","sTR4","sTRX4","2 x G34","2 x LGA1366","2 x LGA2011","2 x LGA2011-3","2 x LGA2011-3 Narrow","Integrated Atom","Integrated Celeron","Integrated Pentium","Integrated Xeon","Integrated E-Series","Integrated C-Series","Integrated A4-5000","Integrated Athlon II X2 215"]        
    for socket in soc:
        motherBoard_Socket.objects.create(name=socket)
    return JsonResponse("success!!",safe=False)



def init_form_factor(request):
    
    for FormF in Form_Factor.objects.all():
                FormF.delete()
    
    ff = ["ATX","MicroATX","MiniITX","ThinMiniITX","MiniDTX","FlexATX","EATX","XLATX","HPTX","SSICEB","SSIEEB"]        
    for form_factor in ff:
        Form_Factor.objects.create(name=form_factor)
    return JsonResponse("success!!",safe=False)




def init_radiator_siz(request):
    
    for Rad in Radiator_size.objects.all():
                Rad.delete()
    
    rad = ["120","240","280","360","420","+480"]        
    for rsize in rad:
        Radiator_size.objects.create(size=rsize)
    return JsonResponse("success!!",safe=False)



def reset_dataBase(request):
    resaults = ""
    #resaults+=load_Cases(request).context
    
    
    
    
    resaults+=f"reinitialization motherboard socket : {init_motherBoardSocket(request).content.decode('utf-8')}    , "
    resaults+=f"reinitialization form factors : {init_form_factor(request).content.decode('utf-8')}    , "
    resaults+=f"reinitialization r.size : {init_radiator_siz(request).content.decode('utf-8')}    , "
    return JsonResponse(resaults,safe=False)
    
    resaults+=f"load Case : {load_Cases(request).content.decode('utf-8')}    , "
    resaults+=f"load CaseAccessorys : {load_Case_accessorys(request).content.decode('utf-8')}    , "
    resaults+=f"load CaseFans : {load_Case_Fans(request).content.decode('utf-8')}    , "
    resaults+=f"load Cpu_Cooler : {load_Cpu_Cooler(request).content.decode('utf-8')}    , "
    resaults+=f"load Cpus : {load_Cpus(request).content.decode('utf-8')}    , "
    resaults+=f"load_External_Hard_Drive : {load_External_Hard_Drive(request).content.decode('utf-8')}    , "
    resaults+=f"load_Internal_Hard_Drive : {load_Internal_Hard_Drive(request).content.decode('utf-8')}    , "
    resaults+=f"load_Fan_Controller : {load_Fan_Controller(request).content.decode('utf-8')}    , "
    resaults+=f"load_Headphones : {load_Headphones(request).content.decode('utf-8')}    , "
    resaults+=f"load_Keyboard : {load_Keyboard(request).content.decode('utf-8')}    , "
    resaults+=f"load_Memory : {load_Memory(request).content.decode('utf-8')}    , "
    resaults+=f"load_MotherBoard : {load_MotherBoard(request).content.decode('utf-8')}    , "
    resaults+=f"load_Monitor : {load_Monitor(request).content.decode('utf-8')}    , "
    resaults+=f"load_Mouse : {load_Mouse(request).content.decode('utf-8')}    , "
    resaults+=f"load_OpticalDrive : {load_OpticalDrive(request).content.decode('utf-8')}    , "
    resaults+=f"load_PowerSupply : {load_PowerSupply(request).content.decode('utf-8')}    , "
    resaults+=f"load_SoundCard : {load_SoundCard(request).content.decode('utf-8')}    , "
    resaults+=f"load_Speakers : {load_Speakers(request).content.decode('utf-8')}    , "
    resaults+=f"load_ThermalPaste : {load_ThermalPaste(request).content.decode('utf-8')}    , "
    resaults+=f"load_VideoCard : {load_VideoCard(request).content.decode('utf-8')}    , "
    resaults+=f"load_Webcam : {load_Webcam(request).content.decode('utf-8')}    , "
    resaults+=f"load_WiresNetworkCard : {load_WiresNetworkCard(request).content.decode('utf-8')}    , "
    resaults+=f"load_WirelessNetworkCard : {load_WirelessNetworkCard(request).content.decode('utf-8')} "
    
    return JsonResponse(resaults,safe=False)
    
    


class RCaseAcc(generics.RetrieveAPIView):
    serializer_class = CaseAccessorySerializer
    queryset = CaseAccessory.objects.all()
    lookup_field = 'id'



'''

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


# مسار ChromeDriver
CHROME_DRIVER_PATH = "chromedriver-win64\chromedriver.exe"

# مجلد لحفظ الصور
SAVE_FOLDER = "D:/downloads"
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)
import os
import requests
import json
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from django.http import JsonResponse

# إعداد مجلد حفظ الصور
SAVE_FOLDER = "D:/downloads"
os.makedirs(SAVE_FOLDER, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def is_valid_image(url):
    """التحقق مما إذا كان الرابط يحتوي على صورة حقيقية"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200 and "image" in response.headers["Content-Type"]:
            return True
    except Exception:
        return False
    return False

def get_high_res_images(search_term):
    """استخراج روابط الصور عالية الدقة من Bing"""
    search_url = f"https://www.bing.com/images/search?q={search_term}&form=HDRSC2"
    response = requests.get(search_url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    scripts = soup.find_all("script")

    image_urls = []
    for script in scripts:
        if "murl" in script.text:
            try:
                json_text = script.text.split("var s=")[-1].split(";</script>")[0]
                data = json.loads(json_text)
                for item in data["value"]:
                    img_url = item.get("contentUrl")
                    if img_url:
                        image_urls.append(img_url)
            except Exception:
                continue

    return image_urls

def download_high_res_image(request):
    try:
        motherboards = [
            "ASUS ROG Strix B550-F Gaming",
            "MSI MAG B550 Tomahawk",
            "Gigabyte B550 AORUS Elite"
        ]

        paths = {}

        for mb in motherboards:
            image_urls = get_high_res_images(mb)

            found_image = False
            for img_url in image_urls:
                if is_valid_image(img_url):
                    try:
                        img_response = requests.get(img_url, headers=HEADERS, timeout=10)
                        if img_response.status_code == 200:
                            image = Image.open(BytesIO(img_response.content))
                            if image.width > 800:  # التحقق من الدقة العالية
                                image_path = os.path.join(SAVE_FOLDER, f"{mb.replace(' ', '_')}.jpg")
                                image.save(image_path, "JPEG")
                                paths[mb] = image_path
                                found_image = True
                                break
                    except Exception as e:
                        paths[mb] = f"Failed to process image: {str(e)}"

            if not found_image:
                paths[mb] = "No high-resolution image found"

        return JsonResponse({"status": "success", "paths": paths})

    except Exception as ex:
        return JsonResponse({"status": "error", "message": str(ex)})
        
        
        '''
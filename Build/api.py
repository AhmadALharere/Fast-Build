from PcPart.models import Part,power_supply_and_cases,Form_Factor
from django.http import JsonResponse
from Cart.api import check_discount
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from PcPart.models import Part,MotherBoard,Case,CaseFan,Cpu,CpuCooler,Memory,InternalHardDrive,PowerSupply,VideoCard
from django.db.models import Q
from home.serializers import PartSerializer
from functools import reduce
from operator import and_
from rest_framework.response import Response

def compatibility_Case_MotherBoard(Case,MotherBoard):#danger if it False
    return (MotherBoard[0].form_Factor in Case[0].form_factor_support.all())

def compatibility_Case_CaseFan(Case,CaseFans):#Warning if it False
    fans_with_size={'120':0,'140':0}
    for fan in CaseFans:
        fans_with_size[str(fan.size)]+=1
    return True if Case[0].fan_120mm_support >= fans_with_size['120'] +fans_with_size['140']  and Case[0].fan_140mm_support >= fans_with_size['140'] else False

def compatibility_Case_CPUCooler(Case,CPUCooler):#danger if it False
    if CPUCooler[0].type == 'Liquid Cooler':

        return True if Case[0].radiator_support == CPUCooler[0].size else False        
    
    return True if Case[0].cpu_cooler_clearance >= CPUCooler[0].size else False

def compatibility_Case_InternalHardDrive(Case,InternalHardDrive):#Warning if it False
    IHD_with_size=[0,0]#3.5,2.5
    for hard_drive in InternalHardDrive:
        if hard_drive.type == "HDD SATA" or hard_drive.type == "HDD SAS":
            IHD_with_size[0]+=1
        else:
            IHD_with_size[1]+=1
    return True if Case[0].socket3_5 >= IHD_with_size[0] and Case[0].socket2_5 >= IHD_with_size[1] else False

def compatibility_Case_PowerSupply(Case,PowerSupply):#Danger if it False
    if Case[0].psu =="Not Included":#Not Included
        if Case[0].type in power_supply_and_cases[PowerSupply[0].type]:
            return True
    return False

def compatibility_Case_VideoCard(Case,VideoCard):#Danger if it False
    return True if VideoCard[0].length <= Case[0].gpu_clearance else False

def compatibility_CaseFan(CaseFans,MotherBoard):#Warning if it False
    return True if CaseFans.__len__()<=MotherBoard[0].fan_headers else False

def compatibility_MotherBoard_CPU(MotherBoard,CPU):#Danger if it False
    return True if MotherBoard[0].socket==CPU[0].socket else False

def compatibility_MotherBoard_Memory(MotherBoard,Memorys):#Danger if it False
    if MotherBoard[0].memory_Slots>=Memorys.__len__():
        full_capacity = 0
        Max_Capacity = Memorys[0].total_capacity
        DDRVer = Memorys[0].generation
        is_all_same_ddrVer = True
        unique_memorys={}
        for unit in Memorys:
            full_capacity+=unit.total_capacity
            if unit.total_capacity>Max_Capacity:
                Max_Capacity=unit.total_capacity
            if unit.generation!=DDRVer:
                is_all_same_ddrVer=False
            if str(unit.id) not in unique_memorys.keys():
                unique_memorys[str(unit.id)]=1
            else:
                unique_memorys[str(unit.id)]+=1
        
        if is_all_same_ddrVer:
            if MotherBoard[0].supported_ddr_version==DDRVer:
                print('test')
        
                if Max_Capacity<=MotherBoard[0].max_capacity_per_slot:
                    if full_capacity<=MotherBoard[0].max_Memory:
                        UM_num=len(unique_memorys.keys())
                        print('test')
    
                        if (MotherBoard[0].memory_channels=="Single Channel") or (MotherBoard[0].memory_channels=="Dual Channel" and UM_num<=MotherBoard[0].memory_Slots/2) or (MotherBoard[0].memory_channels=="Quad Channel" and UM_num<=MotherBoard[0].memory_Slots/4):
                            return True
        return False
        
def compatibility_MotherBoard_CPUCooler(MotherBoard,CPUCooler):#Danger if it False
    if CPUCooler[0].type == "Liquid Cooler":
        return MotherBoard[0].aio_support
    return True

def compatibility_MotherBoard_InternalHardDrives(MotherBoard,InternalHardDrives):#Warning if it False
    hard_count=[0,0]#sata/m2
    for hardDrive in InternalHardDrives:
        if hardDrive.type=="SSD M.2":
            hard_count[1]+=1
        elif hardDrive.type!="SSD NVMe":
            hard_count[0]+=1
    return True if MotherBoard[0].m2_slot>=hard_count[1] and MotherBoard[0].sata_ports>=hard_count[0] else False

def compatibility_MotherBoard_Extension_Cards(MotherBoard,SoundCard,VideoCard,WiresNetworkCard,WirelessNetworkCard,IHD):#Warning if it false
        EC_counters = 0
        NVMe_list = []
        for hard in IHD:
            if hard.type =="SSD NVMe":
                NVMe_list.append(hard)
        
        for cardList in [SoundCard,VideoCard,WiresNetworkCard,WirelessNetworkCard,NVMe_list]:
            EC_counters+=len(cardList)
        
        return True if MotherBoard[0].pcie_slots>=EC_counters else False  
  
def compatibility_CPU_Memory(CPU,Memorys):#Danger if it false
        max_memory = 0
        for memory in Memorys:
            max_memory+=memory.total_capacity
        return CPU[0].max_memory_support>=max_memory

def compatibility_PowerSupply(partList):# 2: success,1:warning,0:danger
    total_power = 0
    for parts in partList.values():
        for part in parts:
            total_power+=part.power_requirement
    # 2: success,1:warning,0:danger
    return 2 if partList['powersupply'][0].wattage>=total_power*1.25 else (1 if partList['powersupply'][0].wattage>=total_power else 0 )


PC_main_keys = ['case',
        'casefan',
        'cpu',
        'cpucooler',
        'motherboard',
        'internalharddrive',
        'memory',
        'powersupply',
        'videocard']

class PC_Collection():
    compatibility_status=['Undefined','Danger','Warning','Success']
    def __init__(self,partList):
        self.part_sorter={
        'case':[],
        'casefan':[],
        'cpu':[],
        'cpucooler':[],
        'motherboard':[],
        'internalharddrive':[],
        'memory':[],
        'powersupply':[],
        'videocard':[],
        }
        self.section_price={
        'case':0,
        'casefan':0,
        'cpu':0,
        'cpucooler':0,
        'motherboard':0,
        'internalharddrive':0,
        'memory':0,
        'powersupply':0,
        'videocard':0,
        }
        self.total_cost = 0
        for part in partList:
            
            self.part_sorter["".join(part.content_type.name.strip().split(" "))].append(part)
            discount_status=check_discount(part)
            part.price = discount_status[1] if discount_status[0] else part.price
            self.total_cost += part.price
            self.section_price["".join(part.content_type.name.strip().split(" "))]+=part.price
        self.Collection_Test()

    
    def add_part(self,part):
        self.part_sorter[part.content_type.name].append(part)
        discount_status=check_discount(part)
        part.price = discount_status[1] if discount_status[0] else part.price
        self.total_cost += part.price
        self.section_price[part.content_type.name]+=part.price
        self.Collection_Test()
    def remove_part(self,part):
        if part in self.part_sorter[part.content_type.name]:
            discount_status=check_discount(part)
            self.total_cost -= discount_status[1] if discount_status[0] else part.price
            self.part_sorter[part.content_type.name].remove(part)
            self.section_price[part.content_type.name]-=part.price
            self.Collection_Test()
            
    def Collection_Test(self):
        
        self.is_collection_valid = True
        self.compatibility = PC_Collection.compatibility_status[0]
                
        for keys in ['case',
                    'cpu',
                    'cpucooler',
                    'motherboard',
                    'powersupply']:
            if len(self.part_sorter[keys])!= 1:
                self.is_collection_valid = False
                self.compatibility = PC_Collection.compatibility_status[0]
                self.message = f'this cart is not represent a PC collection because there is {len(self.part_sorter[keys])} {keys}s in it,if you want to build a PC then pick just one of {keys} kategory'
                return False
        for keys in ['casefan',
                    'internalharddrive',
                    'memory'
                    ]:

            if len(self.part_sorter[keys]) < 1:
                self.is_collection_valid = False
                self.compatibility = PC_Collection.compatibility_status[0]
                self.message = f'this cart is not represent a PC collection because there is NO {len(self.part_sorter[keys])} {keys}s in it,if you want to build a PC then pick at least one of {keys} category'
                return False
        
        if not compatibility_MotherBoard_CPU(self.part_sorter['motherboard'],self.part_sorter['cpu']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the MotherBoard and CPU is not compatible'
            return False
            
        elif not compatibility_MotherBoard_Memory(self.part_sorter['motherboard'],self.part_sorter['memory']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the MotherBoard can`t be compilable with all selected Memory'
            return False
        
        elif not compatibility_Case_MotherBoard(self.part_sorter['case'],self.part_sorter['motherboard']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the Case cannot contain this MotherBoard'
            return False

        elif not compatibility_Case_PowerSupply(self.part_sorter['case'],self.part_sorter['powersupply']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the Case cannot contain PowerSupply or it has already one i it'
            return False
        
        elif not compatibility_MotherBoard_CPUCooler(self.part_sorter['motherboard'],self.part_sorter['cpucooler']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the MotherBoard is not supported Lequid Cooler'
            return False

        elif not compatibility_Case_VideoCard(self.part_sorter['case'],self.part_sorter['videocard']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the Case maybe cannot contain GPU Card'
            return False

        elif not compatibility_Case_CPUCooler(self.part_sorter['case'],self.part_sorter['cpucooler']):
            self.compatibility = PC_Collection.compatibility_status[1]
            self.message = 'the Case maybe cannot contain CPU Cooler'
            return False
            
        elif not compatibility_MotherBoard_Extension_Cards(self.part_sorter['motherboard'],[],self.part_sorter['videocard'],[],[],self.part_sorter['internalharddrive']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'the MotherBoard don`t have enough or suitable slots to import all Extension Cards'
            return False
            
        elif not compatibility_MotherBoard_InternalHardDrives(self.part_sorter['motherboard'],self.part_sorter['internalharddrive']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'the MotherBoard don`t have enough or suitable slots to import all Hard Drives'
            return False

        elif not compatibility_Case_InternalHardDrive(self.part_sorter['case'],self.part_sorter['internalharddrive']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'the Case maybe cannot contain all Hard-Drives'
            return False

        elif not compatibility_Case_CaseFan(self.part_sorter['case'],self.part_sorter['casefan']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'the Case maybe cannot contain all Fans'
            return False

        elif not compatibility_CaseFan(self.part_sorter['casefan'],self.part_sorter['motherboard']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'there is no enough channels to connect all Fans'
            return False

        elif not compatibility_CPU_Memory(self.part_sorter['cpu'],self.part_sorter['memory']):
            self.compatibility = PC_Collection.compatibility_status[2]
            self.message = 'The CPU cannot deal with all this memory'
            return False

        else:
            results = compatibility_PowerSupply(self.part_sorter)
            if results==1:
                self.compatibility = PC_Collection.compatibility_status[2]
                self.message = 'power supply may have shortage in power sometimes,prefer to keep always a 20 persent avilable wattage'
                return False
            elif results==0:
                self.compatibility = PC_Collection.compatibility_status[1]
                self.message = 'power supply cannot provide the required wattage for your PC'
                return False
            
        self.compatibility = PC_Collection.compatibility_status[3]
        self.message = 'The part that you had selected must be fit together'
        return True

    '''
    ['case',
        'casefan',
        'cpu',
        'cpucooler',
        'motherboard',
        'internalharddrive',
        'memory',
        'powersupply',
        'videocard']
    '''
    '''
    ['case' , 'cpu' , 'videocard' , 'motherboard' , 'powersupply' , 'casefan' , 'cpucooler' , 'internalharddrive' , 'memory']
    
    '''
class PC_Chooser():
    budget_divide = {
    "Gaming":{
        "class A":[0.07,0.25,0.25,0.08,0.13,0.04,0.04,0.08,0.06],# 900<budget
        "class B":[0.08,0.19,0.25,0.09,0.15,0.04,0.04,0.09,0.07],# 550<budget<900
        "class C":[0.08,0.20,0.25,0.11,0.15,0.07,0.00,0.07,0.07]# budget<550
    }# budget > 450
    ,
    "Video Editing":{
        "class A":[0.06,0.20,0.26,0.10,0.12,0.04,0.03,0.10,0.08],# 1200<budget
        "class B":[0.06,0.22,0.26,0.10,0.13,0.04,0.03,0.08,0.08],# 700<budget<1200
        "class C":[0.06,0.23,0.30,0.10,0.13,0.04,0.02,0.06,0.06]# budget<700
    }# budget > 550
    ,
    "Developer":{
        "class A":[0.07,0.30,0.20,0.07,0.14,0.03,0.04,0.07,0.08],# 800<budget
        "class B":[0.08,0.30,0.15,0.08,0.15,0.04,0.04,0.08,0.08],# 500<budget<800 
        "class C":[0.10,0.35,0.00,0.10,0.18,0.05,0.05,0.09,0.08]# budget<500
    }# budget > 400
    ,
    "Office":{
        "class A":[0.10,0.20,0.15,0.10,0.12,0.00,0.07,0.16,0.10],#500<budget
        "class B":[0.10,0.28,0.00,0.10,0.17,0.00,0.10,0.15,0.10],# 300<budget<500
        "class C":[0.10,0.30,0.00,0.15,0.20,0.00,0.00,0.15,0.10]# budget<300
    }# budget > 200
    
    
}
    
    def __init__(self,budget,pc_type,partList):
        self.part_budget={
        'case':0,
        'casefan':0,
        'cpu':0,
        'cpucooler':0,
        'motherboard':0,
        'internalharddrive':0,
        'memory':0,
        'powersupply':0,
        'videocard':0,
        }
        self.pc_type = pc_type
        self.budget = budget
        self.pc_class = 'class C'
        self.free_budget = 0 #this field is used to store any free values in a section`s budget after selecting a piece from it
        self.PC = PC_Collection(partList)
        self.set_pc_class()
        self.budget_divider()
        
    def set_pc_class(self):
            if self.pc_type=='Gaming':
                self.pc_class = 'class A' if self.budget > 900 else 'class B' if self.budget>550 else 'class C'
            elif self.pc_type=='Developer':
                 self.pc_class = 'class A' if self.budget > 800 else 'class B' if self.budget>500 else 'class C'
            elif self.pc_type=='Video Editing':
                 self.pc_class = 'class A' if self.budget > 1200 else 'class B' if self.budget>700 else 'class C'
            else:
                 self.pc_class = 'class A' if self.budget > 500 else 'class B' if self.budget>300 else 'class C'
       
        
    def budget_divider(self):
        divide_rate = PC_Chooser.budget_divide[self.pc_type][self.pc_class]
        for key,rate in zip(['case','cpu','videocard','motherboard','powersupply','casefan','cpucooler','internalharddrive','memory'],divide_rate):
            if self.PC.section_price[key]!=0:
                self.free_budget+=self.budget * rate - self.PC.section_price[key]
                
            else :
                self.part_budget[key]=self.budget * rate
            
# motherboard > case > cpu > gpu > ram > hard > cpufan > casefan > power supply
    
def get_filtered_queryset(chooser,ordered_part):
    limit = {'piece':1}
    print(f"free budget: {chooser.free_budget} , section budget: {chooser.part_budget[ordered_part]} , total: {chooser.part_budget[ordered_part]+chooser.free_budget}")
    price_filter = Q(price__lte=chooser.part_budget[ordered_part]+chooser.free_budget)
    if ordered_part=='motherboard':
        return MotherBoard.objects.filter(price_filter).order_by('-population'),limit
    elif ordered_part=='case':
        return Case.objects.filter(price_filter & Q(form_factor_support=chooser.PC.part_sorter['motherboard'][0].form_Factor)).order_by('-population'),limit
    elif ordered_part=='cpu':
        return Cpu.objects.filter(price_filter & Q(socket=chooser.PC.part_sorter['motherboard'][0].socket)).order_by('-population'),limit
    elif ordered_part=='videocard':
        limit['piece'] = chooser.PC.part_sorter['motherboard'][0].pcie_slots
        motherboard_con = Q(compatible_motherboard = chooser.PC.part_sorter['motherboard'][0].socket)
        case_con = Q(length__lte=chooser.PC.part_sorter['case'][0].gpu_clearance)
        return VideoCard.objects.filter(price_filter & motherboard_con & case_con).order_by('-population'),limit
    elif ordered_part=='memory':
        limit['piece'] = chooser.PC.part_sorter['motherboard'][0].pcie_slots
        cpu_con = Q(total_capacity__lte = chooser.PC.part_sorter['cpu'][0].max_memory_support)
        motherboard_con_1 = Q(generation = chooser.PC.part_sorter['motherboard'][0].supported_ddr_version)
        motherboard_con_2 = Q(total_capacity__lte = chooser.PC.part_sorter['motherboard'][0].max_capacity_per_slot)
        motherboard_con_3 = Q(total_capacity__lte = chooser.PC.part_sorter['motherboard'][0].max_Memory)
        return Memory.objects.filter(price_filter & cpu_con & motherboard_con_1 & motherboard_con_2 & motherboard_con_3).order_by('-population'),limit
    elif ordered_part=='internalharddrive':
        if chooser.PC.part_sorter['motherboard'][0].m2_slot:
            limit = {'SATA':chooser.PC.part_sorter['motherboard'][0].sata_ports,'MVMe':chooser.PC.part_sorter['motherboard'][0].pcie_slots - len(chooser.PC.part_sorter['videocard']),'m.2':chooser.PC.part_sorter['motherboard'][0].m2_slot}
            return InternalHardDrive.objects.filter(price_filter).order_by('-population'),limit
        else:
            no_m2_con = Q(type !='SSD M.2')
            return InternalHardDrive.objects.filter(price_filter & no_m2_con).order_by('-population'),limit
    
    elif ordered_part=='cpucooler':
        motherboard_con = Q(compatibility = chooser.PC.part_sorter['motherboard'][0].socket)
        case_con_1 = Q(size = chooser.PC.part_sorter['case'][0].radiator_support)
        case_con_2 = Q(cooler_height__lte = chooser.PC.part_sorter['case'][0].cpu_cooler_clearance)
        liquid_con = Q(type='Liquid Cooler')
        if chooser.PC.part_sorter['motherboard'][0].aio_support:
            return CpuCooler.objects.filter(price_filter & ((case_con_2 & case_con_1 & motherboard_con & liquid_con) | (case_con_2 &  motherboard_con & ~liquid_con))).order_by('-population'),limit
        else:
            return CpuCooler.objects.filter(price_filter & case_con_2 & motherboard_con & ~liquid_con).order_by('-population'),limit 
    
    elif ordered_part=='casefan':
        limit={'fan_120mm':chooser.PC.part_sorter['case'][0].fan_120mm_support,'fan_140mm':chooser.PC.part_sorter['case'][0].fan_140mm_support}
        if chooser.PC.part_sorter['case'][0].fan_120mm_support:
            if chooser.PC.part_sorter['case'][0].fan_140mm_support:
                return CaseFan.objects.filter(price_filter).order_by('-population'),limit
            else:
                fan_140mm_con = Q(size=140)
                return CaseFan.objects.filter(price_filter & ~fan_140mm_con).order_by('-population'),limit
        else:
            return None,limit
    else:
        if chooser.PC.part_sorter['case'][0].psu =='Not Included':
            limit['piece'] = 0
            return [],limit
        total_power = 0    
        
        for parts in chooser.PC.part_sorter.values():
            for part in parts:
                total_power += part.power_requirement
        filterlist = []
        filterlist.append(Q(wattage__gte=total_power*1.25))
        filterlist.append(price_filter)
        if len(chooser.PC.part_sorter['videocard'])>1:
             filterlist.append(Q(multi_gpu_support=True))
        if chooser.pc_class in ['Gaming','Video Editing']:
           filterlist.append(Q(efficiency__in=["Gold","Platinum","Titanium"]))
        elif chooser. pc_class=='Developer':
            filterlist.append(Q(efficiency__in=["Bronze","Gold","Platinum","Titanium"]))
        psutype = 'SFX'
        
        if chooser.PC.part_sorter['case'][0].type in power_supply_and_cases['ATX']:
            psutype = 'ATX'
                
        filterlist.append(Q(type = psutype)) 
        combined_filter = reduce(and_,filterlist)
        
        return PowerSupply.objects.filter(combined_filter).order_by('-population') ,limit
         


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def build_pc(request):
    try:
        data = request.data
        budget = data.pop('budget')
        pc_type = data.pop('pc_type')
        ordered_part = data.pop('ordered_part')
        partIdList = data.pop('partList')
        #page_num = request.query_parms.get('page')
        partList = []
        for partId in partIdList:
            partList.append(Part.objects.select_subclasses().get(pk=partId))
    except Part.DoesNotExist as Ex:
        #raise NotFoundErr('error in part id list')    
        return Response(status=400,data={'message':'error in part id list'})
    except Exception as Ex:
        print("exciption in build_pc: "+Ex.__str__())
        return Response(status=400,data={'status':'failed','message':'some main parameters are missing,make sure to send all required parameters in json row body'})
    
    chooser = PC_Chooser(budget,pc_type,partList)
    # motherboard > case > cpu > gpu > ram > hard > cpufan > casefan > power supply
    queryset,limit = get_filtered_queryset(chooser,ordered_part)
    serializer_data = PartSerializer(queryset,many = True)
    return JsonResponse({'statues':'success','query':serializer_data.data,'PC_class':chooser.pc_class,'total_cost':chooser.PC.total_cost,'collection validation':chooser.PC.is_collection_valid,'compatibility_status':chooser.PC.compatibility,'message':chooser.PC.message,'part_limit':limit})
    
    
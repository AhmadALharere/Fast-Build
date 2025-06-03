from rest_framework import generics
from rest_framework.response import Response
from PcPart.models import Part,power_supply_and_cases,Form_Factor
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import order,ShopBasket,Discount
from .serializer import Cart_Serializer,BasketSerializer
from datetime import date

def compatibility_Case_MotherBoard(Case,MotherBoard):#danger if it Flase
    return (MotherBoard.form_Factor in Case.form_factor_support)

def compatibility_Case_CaseFan(Case,CaseFans):#Warning if it Flase
    fans_with_size={'120':0,'140':0}
    for fan in CaseFans:
        fans_with_size[fan.size]+=1
    return True if Case.fan_120mm_support >= fans_with_size['120'] and Case.fan_140mm_support >= fans_with_size['120'] else False

def compatibility_Case_CPUCooler(Case,CPUCooler):#danger if it Flase
    if CPUCooler.type == 'Liquid Cooler':

        return True if Case.radiator_support == CPUCooler.size else False        
    
    return True if Case.cpu_cooler_clearance == CPUCooler.size else False

def compatibility_Case_InternalHardDrive(Case,InternalHardDrive):#Warning if it Flase
    IHD_with_size=[0,0]#3.5,2.5
    for hard_drive in InternalHardDrive:
        if hard_drive.type == "HDD SATA" or hard_drive.type == "HDD SAS":
            IHD_with_size[0]+=1
        else:
            IHD_with_size[1]+=1
    return True if Case.socket3_5 >= IHD_with_size[0] and Case.socket2_5 >= IHD_with_size[1] else False

def compatibility_Case_OpticalDrive(Case,OpticalDrive):#Warning if it Flase
    return True if Case.socket5_25 >= len(OpticalDrive) else False

def compatibility_Case_PowerSupply(Case,PowerSupply):#Danger if it Flase
    if Case.psu =="Not Included":#Not Included
        for formID in Case.form_factor_support:
            if Form_Factor.objects.get(pk=formID).name in power_supply_and_cases[PowerSupply.type]:
                return True
    return False

def compatibility_Case_VideoCard(Case,VideoCard):#Danger if it Flase
    return True if VideoCard.length <= Case.gpu_clearance else False

def compatibility_CaseFan(CaseFans,MotherBoard,FanController):#Warning if it Flase
    if FanController:
        return True if CaseFans.__len__()<=FanController.channels else False
    return True if CaseFans.__len__()<=MotherBoard.fan_headers else False

def compatibility_MotherBoard_CPU(MotherBoard,CPU):#Danger if it Flase
    return True if MotherBoard.socket==CPU.socket else False

def get_motherboard_ddr_ver(str):
    if str in ["DDR","LPDDR"] : return 1
    elif str in ["DDR2","LPDDR2"] : return 2
    elif str in ["DDR3","DDR3L","LPDDR3"] : return 3
    elif str in ["DDR4","DDR4L","LPDDR4","LPDDR4X"] : return 4
    else: return 5

def compatibility_MotherBoard_Memory(MotherBoard,Memorys):#Danger if it Flase
    if MotherBoard.memory_Slots>=Memorys.__len__():
        full_capacity = 0
        Max_Capacity = Memorys[1].total_capacity
        DDRVer = Memorys[1].generation
        is_all_same_ddrVer = True
        unique_memorys={}
        for unit in Memorys:
            full_capacity+=unit.total_capacity
            if unit.total_capacity>Max_Capacity:
                Max_Capacity=unit.total_capacity
            if unit.generation!=DDRVer:
                is_all_same_ddrVer=False
            if unit.id not in unique_memorys.keys:
                unique_memorys[unit.id]=1
            else:
                unique_memorys[unit.id]+=1
        
        if is_all_same_ddrVer:
            if MotherBoard.memory_Slots>=Memorys.__len__():
                if get_motherboard_ddr_ver(MotherBoard.supported_ddr_version)==DDRVer:
                    if Max_Capacity<MotherBoard.max_capacity_per_slot:
                        if full_capacity<MotherBoard.max_Memory:
                            UM_num=unique_memorys.keys.__len__()
                            if (MotherBoard.memory_channels=="Single Channel") or (MotherBoard.memory_channels=="Dual Channel" and UM_num<=MotherBoard.memory_Slots/2) or (MotherBoard.memory_channels=="Quad Channel" and UM_num<=MotherBoard.memory_Slots/4):
                                return True
        return False
        
def compatibility_MotherBoard_CPUCooler(MotherBoard,CPUCooler):#Danger if it Flase
    if CPUCooler.type == "Liquid Cooler":
        return MotherBoard.aio_support
    return True

def compatibility_MotherBoard_InternalHardDrives(MotherBoard,InternalHardDrives):#Warning if it Flase
    hard_count=[0,0]#sata/m2
    for hardDrive in InternalHardDrives:
        if hardDrive.type=="SSD M.2":
            hard_count[2]+=1
        elif hardDrive.type!="SSD NVMe":
            hard_count[1]+=1
    return True if MotherBoard.m2_slut>=hard_count[2] and MotherBoard.sata_ports>=hard_count[1] else False

def compatibility_MotherBoard_Extension_Cards(MotherBoard,SoundCard,VideoCard,WiresNetworkCard,WirelessNetworkCard,InternalHardDrive):#Warning if it false
        NVMe_hards = []
        for hard in InternalHardDrive:
            if hard.type == "SSD NVMe":
                NVMe_hards.append(hard)
        EC_counters = len(VideoCard)+len(SoundCard)+len(WiresNetworkCard)+len(WirelessNetworkCard)+len(NVMe_hards)
        return True if MotherBoard.pcie_slots>=EC_counters else False
    
def compatibility_CPU_Cooling(CPU):#Warning if it false
        return not(CPU.cooling_included)
    
def compatibility_CPU_Memory(CPU,Memorys):#Danger if it false
        return CPU.max_memory_support>=Memorys.__len__()


def check_discount(part):
    outputs = [False,0]
    try:
        discount = Discount.objects.get(part=part)
    except Discount.DoesNotExist:
        return outputs#state,price
    today = date.today()
    
    if discount.is_valid:
        if discount.start_date<=today and discount.end_date>=today:
            outputs=[True,discount.new_price]
        else:
            discount.is_valid=False
            discount.save()
            
    return outputs


def get_price(part,is_descount):
    outputs = check_discount(part)
    if outputs[0]:
        return [is_descount==True,outputs[1]]
    else:
        return [is_descount==False,part.price]


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt  # هنا يكون فعال لأنك خارج ال APIView class
def is_collection_valid(request):
        part_sorter={
        'Case':[],
        'CaseAccessory':[],
        'CaseFan':[],
        'Cpu':[],
        'CPUCooler':[],
        'MotherBoart':[],
        'ExternalHardDrive':[],
        'InternalHardDrive':[],
        'FanController':[],
        'Headphones':[],
        'Keyboard':[],
        'Memory':[],
        'Monitor':[],
        'OpticalDrive':[],
        'Mouse':[],
        'PowerSupply':[],
        'SoundCard':[],
        'Speakers':[],
        'ThermalPaste':[],
        'VideoCard':[],
        'Webcam':[],
        'WiresNetworkCard':[],
        'WirelessNetworkCard':[]
        }
        try:

            data = request.data
            # data = json.load(request.body)
            print(data)
            for partID,num in data:
                unit = Part.objects.select_subclasses().get(pk=partID)
                unit_type=type(unit).__name__
                
                while num>0:
                    part_sorter[unit_type].append(unit)
                    num-=1
                    
        except Exception as Ex:
                print(f'Exciption:{Ex}/nAPI: Is_collection_Valid/ndata:{data}')
                return JsonResponse({'status':'Failed','compatibility':'Undefined','message':'Exception has been detecated'})
        for keys in ['Case',
                    'Cpu',
                    'CPUCooler',
                    'MotherBoart',
                    'PowerSupply']:
            if len(part_sorter[keys])!= 1:
                return JsonResponse({'status':'Failed','compatibility':'Undefined','message':f'this cart is not represent a PC collection because there is {len(part_sorter[keys])} {keys}s in it,if you want to build a PC then pick just one of {keys} kategory'})
            
        for keys in ['CaseFan',
                    'InternalHardDrive',
                    'Memory'
                    ]:

            if len(part_sorter[keys]) < 1:
                return JsonResponse({'status':'Failed','compatibility':'Undefined','message':f'this cart is not represent a PC collection because there is NO {len(part_sorter[keys])} {keys}s in it,if you want to build a PC then pick at least one of {keys} kategory'})

        if not compatibility_MotherBoard_CPU(part_sorter['MotherBoard'],part_sorter['CPU']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the MotherBoard and CPU isnot compitable'})

        if not compatibility_MotherBoard_Memory(part_sorter['MotherBoard'],part_sorter['Memory']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the MotherBoard can`t be compitable with all selected Memorys'})

        if not compatibility_Case_MotherBoard(part_sorter['Case'],part_sorter['MotherBoard']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the Case cannot contain MotherBoard'})

        if not compatibility_Case_PowerSupply(part_sorter['Case'],part_sorter['PowerSupply']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the Case cannot contain PowerSupply or it has already one i it'})

        if not compatibility_MotherBoard_CPUCooler(part_sorter['MotherBoard'],part_sorter['CPUCooler']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the MotherBoard is not supported Lequid Cooler'})

        if not compatibility_Case_VideoCard(part_sorter['Case'],part_sorter['VideoCard']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the Case maybe cannot contain GPU Card'})

        if not compatibility_Case_CPUCooler(part_sorter['Case'],part_sorter['CPUCooler']):
            return JsonResponse({'status':'Success','compatibility':'Danger','message':'the Case maybe cannot contain CPU Cooler'})
            
        if not compatibility_MotherBoard_Extension_Cards(part_sorter['MotherBoard'],part_sorter['SoundCard'],part_sorter['VideoCard'],part_sorter['WiresNetworkCard'],part_sorter['WirelessNetworkCard']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'the MotherBoard don`t have enough or suitable sluts to import all Extintial Cards'})
            
        if not compatibility_MotherBoard_InternalHardDrives(part_sorter['MotherBoard'],part_sorter['InternalHardDrive']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'the MotherBoard don`t have enough or suitable sluts to import all Hard Drives'})

        if not compatibility_Case_InternalHardDrive(part_sorter['Case'],part_sorter['InternalHardDrive']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'the Case maybe cannot contain all Hard-Drives'})

        if not compatibility_Case_OpticalDrive(part_sorter['Case'],part_sorter['OpticalDrive']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'the Case maybe cannot contain all OpticalDrive'})

        if not compatibility_Case_CaseFan(part_sorter['Case'],part_sorter['CaseFan']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'the Case maybe cannot contain all Fans'})

        if not compatibility_CaseFan(part_sorter['CaseFan'],part_sorter['MotherBoard'],part_sorter['FanController']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'there is no enough channels to connect all Fans'})

        if not compatibility_CPU_Memory(part_sorter['CPU'],part_sorter['Memory']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'The CPU cannot deal with all this memory'})

        if not compatibility_CPU_Cooling(part_sorter['CPU']):
            return JsonResponse({'status':'Success','compatibility':'Warning','message':'The CPU has already cooler with it'})


        return JsonResponse({'status':'Success','compatibility':'Success','message':'The part that you had selected must be fit togather'})



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt  # هنا يكون فعال لأنك خارج ال APIView class
def Order_Cart(request):
    data = request.data
    parts = []
    try:
        for unit in data:#unpack and get data from database
            parts.append([Part.objects.get(pk=unit[0]),unit[1],unit[2]==1])    
    except Exception as Ex:
        print(f'Exciption:{Ex}/nAPI: Order_Cart/ndata:{data}')
        return JsonResponse({"status":"failed","message":"Exception has been detecated while doing your order,please try again"}) 
               
    for part in parts:#test if there is enough piece in the storage
        if part[0].in_storage >= part[1]:
              part[0].in_storage-=part[1]
              part[0].population+=part[1]
        else:
            return JsonResponse({"status":"failed","message":f"sorry but there is no enough piece of {part[0].name} in shop storage, yow can now only order {part[0].in_storage}"})
    prices = []
    for part in parts:
        price_data = get_price(part[0],part[2])
        if part[2]!=price_data[0]:
            if part[2]:
                return JsonResponse({"status":"failed","message":f"the discount in piece {part[0].name} has been disapeared , it`s price now is {part[0].price}$"})
        prices.append([price_data[0],price_data[1]])
        


    cart = ShopBasket.objects.create(
    client = request.user,
    total_cost = 0,
    state = "Waiting") 
    i = 0
    for part in parts:
        part[0].save()
        order.objects.create(basket = cart,
                    product = part[0],
                    quantity = part[1],
                    price=prices[i][1])
        
        cart.total_cost+= prices[i][1]*part[1]
        i+=1
    cart.save()
    return JsonResponse({"status":"success","message":"order has been done successfully"})
            

class Cart_list(generics.ListAPIView):
    serializer_class=Cart_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]                                   
    def get_queryset(self):
        return ShopBasket.objects.filter(client=self.request.user).order_by('-order_date')




class Cart_Details(generics.RetrieveDestroyAPIView):
    serializer_class=BasketSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]                                   
    def get_queryset(self):
        return ShopBasket.objects.filter(client=self.request.user)


@api_view(['POST'])
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def Cancel_Cart(request,id):
    try:
        cart = ShopBasket.objects.filter(client=request.user).get(pk=id)
        if cart.state in ["Done","Canceled","Rejected"]:
            return Response(status=HTTP_400_BAD_REQUEST,data={'message':f" can not cancle cart with state {cart.state} , it must be ether \" waiting \" or \" Ready \" to cancel"})
        cart.state="Canceled"
        cart.save()
        return Response(status=HTTP_200_OK,data={'message':"wanted cart canceled Successfully!"})
    except ShopBasket.NotFoundErr as Ex:
        return Response(status=HTTP_404_NOT_FOUND,data={'message':"you do not have any Cart like this!"})
    
        
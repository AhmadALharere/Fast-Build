from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from PcPart.filters import PartFilter
from PcPart.models import Part
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q
from django.db import transaction
from rest_framework.exceptions import NotFound,PermissionDenied
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.contenttypes.models import ContentType



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def fix_data(request):
    #partList = Part.objects.select_subclasses().all()
    #for id,part in enumerate(partList):
        #part.content_type = ContentType.objects.get_for_model(part)
        #print(f'{id} : {part.id} :: {part.content_type}')
        #part.save
    str = "lrsg operg dgfr"
    print(str.join(str.split()))
        
    return Response({"status":"True"})
    '''
        value = str(type(part)).lower()
        startindex = value.rfind('.')
        endindex = value.rfind('\'')
        value = value[startindex+1:endindex]
        print(value)
        
        
    part.content_type = ContentType.objects.get(Python_Model_Class_Name=Python model class name=Value)
    part.save
    
    '''
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from PcPart.filters import PartFilter
from PcPart.models import Part
from .serializers import PartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class PartListView(generics.ListAPIView):
    queryset = Part.objects.all().order_by('-population')
    serializer_class = PartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]                                   
    filter_backends = [DjangoFilterBackend]
    filterset_class = PartFilter
    
    
    
    
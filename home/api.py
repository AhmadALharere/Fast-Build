from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from PcPart.filters import PartFilter
from PcPart.models import Part
from .serializers import PartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

class part_paginator(PageNumberPagination):
    page_size=20
    page_size_query_param="page_size"
    max_page_size=50




class PartListView(generics.ListAPIView):
    queryset = Part.objects.all().order_by('-population')
    serializer_class = PartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = PartFilter
    pagination_class = part_paginator
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['liked','population','price','date_created']




    
    
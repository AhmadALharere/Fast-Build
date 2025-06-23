from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from PcPart.filters import PartFilter
from PcPart.models import Part
from .serializers import PartSerializer,PartDetailsSerializer,like_Serializer,liked_Part_Serializer,Notification_serializer,Discount_serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Notification,Like,Discount
from django.db.models import Q
from django.db import transaction
from rest_framework.exceptions import NotFound,PermissionDenied
from rest_framework.decorators import api_view, permission_classes, authentication_classes

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
    search_fields = ['name','content_type__model']
    ordering_fields = ['liked','population','price','date_created']


class PartDetailsView(generics.RetrieveAPIView):
    queryset = Part.objects.select_subclasses()
    serializer_class = PartDetailsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'



class LikeListView(generics.ListAPIView):
    serializer_class = liked_Part_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user).order_by('-created_at')
    

class PutLikeView(generics.CreateAPIView):
    serializer_class = like_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        
        part = serializer.validated_data['part']
        
        part.like_count=part.like_count + 1
        part.save()
        serializer.save()


class RemoveLikeView(generics.DestroyAPIView):
    serializer_class = like_Serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        part_id = self.kwargs.get("part_id")
        user = self.request.user

        try:
            return Like.objects.get(part_id=part_id, user=user)
        except Like.DoesNotExist:
            raise NotFound("you don`t have like in this piece or it isn`t exist")

    @transaction.atomic
    def perform_destroy(self, instance):
        part = instance.part
        if part.like_count > 0:
            part.like_count=part.like_count - 1
        else:
            part.like_count=0
        part.save()
        instance.delete()


    
class NotificationListView(generics.ListAPIView):
    serializer_class = Notification_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter((Q(user=self.request.user) | Q(user__isnull=True)) & Q(created_at__gte=self.request.user.date_joined)).order_by('-created_at')
    


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def mark_read_notification(request, id):
    try:
        notification = Notification.objects.get(id=id)
    except Notification.DoesNotExist:
        raise NotFound(detail="Notification not found")

    if notification.user:
        if notification.user != request.user:
            raise PermissionDenied(detail="you have no permission on this notification")
    
    notification.is_read = True
    notification.save()

    return Response({'status': 'Success'})  


class Get_Discount(generics.ListAPIView):
    queryset = Discount.objects.filter(is_valid=True).order_by('-end_date')
    serializer_class = Discount_serializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
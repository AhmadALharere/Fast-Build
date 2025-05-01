from django.urls import include, path
from . import api


urlpatterns = [
    
    
    path('Check-Cart',api.is_collection_valid,name="check compitability"),
    path('order/',api.Order_Cart,name="Order Cart"),
    path('My-Orders/',api.Cart_list.as_view(),name="Order List"),
    path('My-Orders/<int:pk>',api.Cart_Details.as_view(),name="Order Detail"),
]
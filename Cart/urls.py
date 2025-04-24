from django.urls import include, path
from . import api


urlpatterns = [
    
    
    path('Chick-Cart',api.is_collection_valid,name="chick compitability"),
    
]
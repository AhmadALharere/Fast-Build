from django.urls import include, path
from . import api


urlpatterns = [
    
    
    path('Chick-Cart',api.IsCollectionValidAPIView,name="chick compitability"),
    
]
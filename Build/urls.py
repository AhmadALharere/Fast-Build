from django.urls import path
from . import api


urlpatterns = [
    path('build_pc/',api.build_pc,name="Build PC"),
    
]
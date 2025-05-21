from django.urls import path

from . import api


urlpatterns = [
   path("fix",api.fix_data,name="fix"),
]

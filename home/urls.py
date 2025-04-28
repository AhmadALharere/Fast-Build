from django.urls import path
from . import api


urlpatterns = [
    path('Parts/',api.PartListView.as_view(),name="Brause Parts"),
]
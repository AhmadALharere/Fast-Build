from django.urls import path
from . import api


urlpatterns = [
    path('Parts/',api.PartListView.as_view(),name="Browse Parts"),
    path('Parts/<int:id>',api.PartDetailsView.as_view(),name="Part Details"),
]
from django.urls import path
from . import api


urlpatterns = [
    path('Parts/',api.PartListView.as_view(),name="Browse Parts"),
    path('Parts/<int:id>',api.PartDetailsView.as_view(),name="Part Details"),
    path('Like/List',api.LikeListView.as_view(),name="Liked List"),
    path('Like/put',api.PutLikeView.as_view(),name="Put Like"),
    path('Like/remove/<int:part_id>',api.RemoveLikeView.as_view(),name="Remove Like"),
    path('Notification/Load',api.NotificationListView.as_view(),name="Notification List"),
    path('Notification/Read/<int:id>',api.mark_read_notification,name="mark Notification as readed"),
    path('Discount/',api.Get_Discount.as_view(),name="Load Discounts"),
]
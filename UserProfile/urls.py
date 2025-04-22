
from django.urls import path , include
from . import apis



urlpatterns = [
    path('google/',apis.GoogleLogin.as_view(),name ='google-login'),
    path('profile/',apis.profile_info.as_view(),name ='profile-api'),
#    path('profile/',views.showProfile,name ='profile'),
#    path('profile/Edit',views.EditProfile,name ='Edit_profile'),
]



from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import generics , permissions
from rest_framework.response import Response
from .models import profile
from .serializer import Profile_Serializer
from django.contrib.auth.models import User


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000"
    

class profile_info(generics.RetrieveUpdateAPIView):
    
    queryset = profile.objects.select_related('user').all()
    serializer_class = Profile_Serializer
    #lookup_field='user'
    #permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return profile.objects.filter(user=self.request.user)
    
    def get_object(self):
  
        return profile.objects.get(user=self.request.user)
    

     
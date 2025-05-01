from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import generics , permissions
from rest_framework.response import Response
from .models import profile
from .serializer import Profile_Serializer
from django.contrib.auth.models import User
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from rest_framework.exceptions import AuthenticationFailed


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000"

    
    def post(self, request, *args, **kwargs):
        try:
            # حاول تنفيذ الـ Social login كالمعتاد
            return super().post(request, *args, **kwargs)
        except OAuth2Error as exc:
            # أي خطأ من Google OAuth2 نصيده هنا
            # نعيد 401 Unauthorized مع رسالة واضحة
            raise AuthenticationFailed(detail="Invalid Google access token.") from exc
    

class profile_info(generics.RetrieveUpdateAPIView):
    
    queryset = profile.objects.select_related('user').all()
    serializer_class = Profile_Serializer
    #lookup_field='user'
    #permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return profile.objects.filter(user=self.request.user)
    
    def get_object(self):
  
        return profile.objects.get(user=self.request.user)
    

     
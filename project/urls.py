"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('UserProfile.urls')),
    path('admin/', admin.site.urls),
    
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # register, email confirm
    path('api-auth/',include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),               # login, logout, password change/reset
    path('api/auth/social/', include('allauth.socialaccount.urls')),      
    path('api/auth/user/', include('UserProfile.urls')),      
    
    path('api/Cart/',include('Cart.urls')),
    path('api/PcParts/',include('PcPart.urls')),
    path('api/home/',include('home.urls')),
    path('api/Build/',include('Build.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

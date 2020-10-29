"""exchange_comparison URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Serializers define the API representation.
from . import settings
from .viewsets import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'idex', IdexViewSet)
router.register(r'bancor', BancorViewSet)
router.register(r'kyber', KyberViewSet)
router.register(r'uniswap', UniswapViewSet)
router.register(r'uniswapone', UniswapOneViewSet)
router.register(r'exchpair', ExchangePairSet, basename='ExchangePair')
router.register(r'trustpair', TrustedPairsSet, basename='TrustedPairs')
router.register(r'settings', SettingsViewSet, basename='settings')
router.register(r'websocket_log', WebsocketLogSet, basename='WebsocketLog')
router.register(r'settings_modules', SettingsModulesViewSet, basename='settings_modules')

urlpatterns = [
                  path('', include(router.urls)),
                  path('contact/', include('send_mail.urls')),
                  path('idex/', include('idex_module.urls')),
                  path('admin/', admin.site.urls),
                  url(r'^api-auth/', include('rest_framework.urls')),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

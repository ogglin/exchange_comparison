from django.urls import path
from . import views

app_name = 'uniswap_module'
urlpatterns = [
    path('', views.uniswap.as_view(), name='uniswap'),
]


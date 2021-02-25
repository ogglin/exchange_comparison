from django.urls import path
from . import views

app_name = 'hitbtc_module'
urlpatterns = [
    path('', views.hitbtc.as_view(), name='hitbtc'),
]


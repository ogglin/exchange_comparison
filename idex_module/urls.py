from django.urls import path
from . import views

app_name = 'idex_module'
urlpatterns = [
    path('', views.idex.as_view(), name='idex'),
]


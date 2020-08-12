from django.urls import path
from . import views
from .getter import *

app_name = 'idex'
urlpatterns = [
    path('', views.idex, name='idex'),
]

# refresh()

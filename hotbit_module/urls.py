from django.urls import path
from . import views

app_name = 'hotbit_module'
urlpatterns = [
    path('', views.hotbit.as_view(), name='hotbit'),
]


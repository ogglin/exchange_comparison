from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactView.as_view(), name='index'),
    path('contact', views.ContactView.as_view(), name='contact'),
]

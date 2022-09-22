from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('getall', views.getcustomers, name = 'GetAll'),
    path('getone/<int:id_>', views.getonecustomer, name = 'GetOne')
]

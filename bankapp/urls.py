from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='Home'),
    path('getall', views.getcustomers, name = 'GetAll'),
    path('getone/<int:id_>', views.getonecustomer, name = 'GetOne'),
    path('add', views.newcustomer, name = 'addOne'),
    path('update/<int:id_>', views.updatecustomer, name = 'Update'),
    path('delete/<int:id_>', views.deletecustomer, name = 'Delete'),
]

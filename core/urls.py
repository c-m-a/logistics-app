from django.contrib import admin
from django.urls import path
from logistics.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customer_list, name="home"),

    path('couriers/', courier_list, name="courier_list"),
    path('couriers/add/', courier_add, name="courier_add"),
    path('couriers/edit/<pk>/', courier_edit, name="courier_edit"),
    path('couriers/delete/<pk>/', courier_delete, name="courier_delete"),

    path('customers/', customer_list, name="customer_list"),
    path('customers/add/', customer_add, name="customer_add"),
    path('customers/edit/<pk>/', customer_edit, name="customer_add"),
    path('customers/delete/<pk>/', customer_delete, name="customer_delete"),
]

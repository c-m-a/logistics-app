from django.contrib import admin
from django.urls import path
from logistics.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customer_list, name="home"),

    path('customers/', customer_list, name="customer_list"),
    path('customers/add/', customer_add, name="customer_add"),
    path('customers/edit/<pk>/', customer_edit, name="customer_add"),
    path('customers/delete/<pk>/', customer_delete, name="customer_delete"),
]

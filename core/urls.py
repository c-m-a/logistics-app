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

    # API REST packages
    path('api/packages/<pk>/assign-courier/<courier_id>', package_assign_courier, name="package_assign_courier"),
    path('api/packages/<pk>/delivered/', package_delivered, name="package_delivered"),
    
    path('packages/', package_list, name="package_list"),
    path('packages/add/', package_add, name="package_add"),
    path('packages/by-courier/', package_by_courier, name="packages_by_courier"),
    path('packages/by-customer/', package_by_customer, name="packages_by_customer"),
    path('packages/edit/<pk>/', package_edit, name="package_edit"),
    path('packages/delete/<pk>/', package_delete, name="package_delete"),
]

from django import forms
from django.db.models import F
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import PackageSerializer

class CourierAddForm(ModelForm):
    class Meta:
        model = Courier
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'phone'}),
        }

class CustomerAddForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'fullname': 'Full name'
        }
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'phone'}),
        }

# Courier CRUD
def courier_add(request):
    form = CourierAddForm()

    if request.method == 'POST':
        form = CourierAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courier_list')

    return render(request, 'couriers/add.html', {
        'form': form,
        'title': 'Add Courier'
    })

def courier_edit(request):
    pass

def courier_delete(request, pk):
    courier = get_object_or_404(Courier, pk=pk)
    courier.delete()
    return redirect('courier_list')

def courier_list(request):
    couriers = Courier.objects.all()
    return render(request, 'couriers/list.html', {
        'couriers': couriers,
        'title': 'Courier List'
    })

# Customer CRUD
def customer_add(request):
    form = CustomerAddForm()

    if request.method == 'POST':
        form = CustomerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')

    return render(request, 'customers/add.html', {'form': form})

def customer_edit(request):
    pass

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {
        'customers': customers,
        'title': 'Customer List'
    })

# Package CRUD
def package_add(request):
    if request.method == 'POST':
        package_form = PackageAddForm(request.POST)
        customer_form = PackageCustomerAddForm(request.POST)

        if package_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save()

            package = package_form.save(commit=False)
            package.sender = customer
            package.save()

            return redirect('package_list')
    else:
        package_form = PackageAddForm()
        customer_form = PackageCustomerAddForm()

    return render(request, 'packages/add.html', {
        'package_form': package_form,
        'customer_form': customer_form,
        'title': 'Create Shipping'
    })

@api_view(['PUT'])
def package_assign_courier(request, pk=None, courier_id=None):
    try:
        package = Package.objects.get(pk=pk)
        courier = Courier.objects.get(pk=courier_id)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)
    except Courier.DoesNotExist:
        return Response({'error': 'Courier not found'}, status=status.HTTP_404_NOT_FOUND)

    package.assigned_courier = courier
    package.status = 'assigned'
    package.save()

    serializer = PackageSerializer(package)
    return Response(serializer.data)
    
@api_view(['PUT'])
def package_delivered(request, pk=None):
    try:
        package = Package.objects.get(pk=pk)
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=status.HTTP_404_NOT_FOUND)

    package.status = 'delivered'
    package.save()

    serializer = PackageSerializer(package)
    return Response(serializer.data)

def package_by_courier(request):
    grouped_pkgs = []
    couriers_with_pkgs = Courier.objects.prefetch_related('assigned_packages')\
        .all()\
        .order_by('id', 'name')

    for courier in couriers_with_pkgs:
        pkgs = courier.assigned_packages.all()
        grouped_pkgs.append({
            'courier': courier,
            'pkgs': pkgs
        })

    return render(
        request,
        'packages/by_courier.html',
        {'grouped_pkgs': grouped_pkgs}
    )

def package_by_customer(request):
    grouped_pkgs = []
    senders_with_pkgs = Customer.objects.prefetch_related('sent_packages')\
        .all()\
        .order_by('id', 'fullname')

    for sender in senders_with_pkgs:
        pkgs = sender.sent_packages.all()
        grouped_pkgs.append({
            'sender': sender,
            'pkgs': pkgs
        })

    return render(
        request,
        'packages/by_customer.html',
        {'grouped_pkgs': grouped_pkgs}
    )

def package_edit(request, pk):
    package = get_object_or_404(Package, pk=pk)
    customer = Customer.objects.get(pk=package.sender.id)

    if request.method == 'POST':
        package_form = PackageAddForm(request.POST, instance=package)
        customer_form = PackageCustomerAddForm(request.POST, instance=customer)

        if package_form.is_valid() and customer_form.is_valid():
            customer = customer_form.save()

            package = package_form.save(commit=False)
            package.sender = customer
            package.save()

            return redirect('package_list')
    else:
        package_form = PackageAddForm(instance=package)
        customer_form = PackageCustomerAddForm(instance=customer)

    return render(request, 'packages/edit.html', {
        'package_form': package_form,
        'customer_form': customer_form,
    })

def package_delete(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    return redirect('package_list')

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'packages/list.html', {'packages': packages})


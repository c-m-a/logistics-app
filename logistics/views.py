from django import forms
from django.forms import ModelForm
from django.shortcuts import render

from .models import *

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


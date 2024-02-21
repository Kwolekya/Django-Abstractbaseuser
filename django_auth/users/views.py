from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from users.forms import (
    CustomerRegistrationForm, EmployeeRegistrationForm, EmployeeUpdateForm,
    CustomerUpdateForm, CustomUserChangeForm,
)
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from users.models import CustomUser, Customer, Employee

# Create your views here.
class HomeView(ListView):
    model = Customer

class RegistrationView(ListView):
    model = CustomUser
    template_name = 'users/register.html'

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            form.save()
            messages.success(request, f'Your account has been created! You can now Login')
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register_customer.html', context)

def register_employee(request):
    if request.method == 'POST':
        r_form = EmployeeRegistrationForm(request.POST)
        if r_form.is_valid():
            email = r_form.cleaned_data.get('email')
            password = r_form.cleaned_data.get('password')
            first_name = r_form.cleaned_data.get('first_name')
            last_name = r_form.cleaned_data.get('last_name')
            r_form.save()
            messages.success(request, f'Your account has been created! You can now Login')
            return redirect('login')
    else:
        r_form = EmployeeRegistrationForm()
    context = {
        'r_form': r_form,
    }
    return render(request, 'users/register_employee.html', context)


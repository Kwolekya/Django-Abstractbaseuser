from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, Customer, Employee

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_customer', 'is_employee')
    list_filter = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_login', 'groups')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_joined')}),
        ('Permissions', {'fields': ('is_customer', 'is_employee', 'is_active', 'is_staff', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('last_name',)
    filter_horizontal = ()

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['employee', 'avatar', 'TIN', 'SSN', 'telephone', 'nationality',]
    list_display = ('employee',)
    list_filter = ['employee',]
    search_fields = ['employee',]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ['customer', 'avatar',]
    list_display = ('customer',)
    list_filter = ['customer',]
    search_fields = ['customer',]
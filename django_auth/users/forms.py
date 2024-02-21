from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from users.models import CustomUser, Customer, Employee

class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField(label = 'Email:',
        widget = forms.EmailInput(
            attrs={
                    'placeholder': 'john@cinemax.com'
            }
        ))
    first_name = forms.CharField(label = 'First Name:',
        widget = forms.TextInput(
            attrs={
                    'placeholder': 'John'
            }
        ))
    last_name = forms.CharField(label = 'Last Name:',
        widget = forms.TextInput(
            attrs={
                    'placeholder': 'Doe'
            }
        ))
    password1 = forms.CharField(label = 'Password:',
        widget = forms.PasswordInput(
            attrs={
                    'placeholder': 'Provide a strong password, at least 8 characters'
            }
        ))
    password2 = forms.CharField(label = 'Confirm Password:',
        widget = forms.PasswordInput(
            attrs={
                    'placeholder': 'Provide same password as above for verification'
            }
        ))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email',  'first_name', 'last_name')

    #def clean_password(self):
    #    # Regardless of what the user provides, return the initial password.
    #    return self.initial["password"]

class CustomerRegistrationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_active = True
        user.save()
        return user

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['avatar',]

class EmployeeRegistrationForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser

    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_active = True
        user.save()
        return user

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['avatar']
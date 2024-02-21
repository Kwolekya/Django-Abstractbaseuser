from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
from PIL import Image
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email')
        if not password:
            raise ValueError('Users must have a password')
        if not first_name:
            raise ValueError('Users must have a first_name')
        if not last_name:
            raise ValueError('Users must have a last_name')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_customeruser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password = password,
            first_name = first_name,
            last_name =last_name,
        )
        user.is_customer = True
        user.save(using=self._db)
        return user

    def create_employeeuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password = password,
            first_name = first_name,
            last_name =last_name,
        )
        user.is_employee = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password = password,
            first_name = first_name,
            last_name =last_name,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password = password,
            first_name = first_name,
            last_name =last_name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField('staff status', default = False)
    is_customer = models.BooleanField('customer status', default = True)
    is_employee = models.BooleanField('employee status', default = False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.email}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_url_full_name(self):
        return f'{self.first_name}-{self.last_name}'

class Employee(models.Model):
    employee = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(default='default.jpg', upload_to='employee_avatars')
    TIN = models.CharField(max_length=16)
    SSN = models.CharField(max_length=16)
    telephone = PhoneNumberField(unique=True)
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.employee}'

    class Meta:
        verbose_name = 'Employee Profile'
        verbose_name_plural = 'Employee Profiles'

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

class Customer(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(default='default.jpg', upload_to='customer_avatars')

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = 'Customer Profile'
        verbose_name_plural = 'Customer Profiles'

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
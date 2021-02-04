from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework.authtoken.admin import User


class LocationModels(models.Model):

    def __str__(self):
        return f'{self.country} - {self.province} - {self.city}'

    country = models.CharField(verbose_name='Country', max_length=100, blank=False)
    province = models.CharField(verbose_name='Province', max_length=100, blank=False)
    city = models.CharField(verbose_name='City', max_length=100, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


class UserActivityModel(models.Model):

    def __str__(self):
        return ''

    activity = models.CharField(verbose_name='Activity', max_length=100, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


class CustomUserModel(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, 'Admin User'),
        (STAFF, 'Staff User'),
    ]

    user = models.OneToOneField(User)
    mobile = models.CharField(verbose_name='Mobile Number', max_length=20, unique=True)
    location = models.ForeignKey(LocationModels, blank=False)
    activity = models.ForeignKey(UserActivityModel, blank=False)
    address = models.TextField(verbose_name='User Address', default=None)
    phone = models.CharField(verbose_name='User Phone', max_length=100)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['mobile', 'location', 'activity', 'address']


class CustomUserManager(BaseUserManager):

    def create_user(self, mobile, location, activity, address, phone):
        if not mobile:
            raise ValueError("User must have Mobile number")
        if not location:
            raise ValueError("User must have Location")
        if not activity:
            raise ValueError("User must have Activity")
        if not address:
            raise ValueError("User must have Address")

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class LocationModel(models.Model):

    def __str__(self):
        return f'{self.country} - {self.province} - {self.city}'

    country = models.CharField(verbose_name='Country', max_length=100, blank=False)
    province = models.CharField(verbose_name='Province', max_length=100, blank=False)
    city = models.CharField(verbose_name='City', max_length=100, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


class UserActivityModel(models.Model):

    def __str__(self):
        return self.activity

    activity = models.CharField(verbose_name='Activity', max_length=100, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)


class CustomUserModel(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(verbose_name='First Name', max_length=50, default='First Name')
    last_name = models.CharField(verbose_name='Last Name', max_length=50, default='Last Name')
    username = models.CharField(verbose_name='Mobile Number', max_length=20, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100)
    location = models.ForeignKey(LocationModel, on_delete=models.CASCADE, default=1)
    activity = models.ForeignKey(UserActivityModel, on_delete=models.CASCADE, default=1)
    address = models.TextField(verbose_name='User Address', default='')
    phone = models.CharField(verbose_name='User Phone', max_length=100, default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

    def save(self, *args, **kwargs):
        self.username = str(self.username)
        super(CustomUserModel, self).save(*args, **kwargs)

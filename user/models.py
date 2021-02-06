from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class LocationModels(models.Model):

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


# class CustomUserManager(UserManager):
#
#     @staticmethod
#     def validate_user(username, password, is_superuser, **extra_fields):
#         if not username:
#             raise ValueError("User name could not be empty")
#
#         if not password:
#             raise ValueError("User Password could not be empty")
#
#         if is_superuser is not True:
#             if extra_fields.get('first_name') is None:
#                 raise ValueError(f'User must have First Name {is_superuser}')
#             if extra_fields.get('last_name') is None:
#                 raise ValueError("User must have Last Name")
#             if extra_fields.get('mobile') is None:
#                 raise ValueError("User must have Mobile")
#             if extra_fields.get('location') is None:
#                 raise ValueError("User must have Location")
#             if extra_fields.get('address') is None:
#                 raise ValueError("User must have Address")
#
#     # def create_user(self, username, email=None, password=None, **extra_fields):
#     #     self.validate_user(username, password, False, **extra_fields)
#     #     user = self.model
#     #     user.first_name = extra_fields.get('first_name')
#     #     user.last_name = extra_fields.get('last_name')
#     #     user.mobile = extra_fields.get('mobile')
#     #     user.set_password(self=self, raw_password=password)
#     #     user.location = extra_fields.get('location')
#     #     user.activity = extra_fields.get('activity')
#     #     user.address = extra_fields.get('address')
#     #     user.phone = extra_fields.get('phone')
#     #     user.is_admin = False
#     #     user.is_staff = False
#     #     user.save(self=self, using=self.db)
#     #     return user
#     #
#     # def create_superuser(self, username, email=None, password=None, **extra_fields):
#     #     self.validate_user(username, password, True, **extra_fields)
#     #     user = self.model
#     #     user.first_name = extra_fields.get('first_name')
#     #     user.last_name = extra_fields.get('last_name')
#     #     user.mobile = extra_fields.get('mobile')
#     #     user.set_password(self=self, raw_password=password)
#     #     # user.location = extra_fields['location']
#     #     # user.activity = extra_fields['activity']
#     #     # user.address = extra_fields['address']
#     #     # user.phone = extra_fields['phone']
#     #     user.is_admin = False
#     #     user.is_staff = False
#     #     user.save(self=self, using=CustomUserModel)
#     #     return user


class CustomUserModel(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(verbose_name='First Name', max_length=50, default='First Name')
    last_name = models.CharField(verbose_name='Last Name', max_length=50, default='Last Name')
    username = models.CharField(verbose_name='Mobile Number', max_length=20, unique=True)
    password = models.CharField(verbose_name='Password', max_length=100)
    location = models.ForeignKey(LocationModels, on_delete=models.CASCADE, default=1)
    activity = models.ForeignKey(UserActivityModel, on_delete=models.CASCADE, default=1)
    address = models.TextField(verbose_name='User Address', default='')
    phone = models.CharField(verbose_name='User Phone', max_length=100, default='')
    create_date = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)

    # USERNAME_FIELD = 'mobile'
    # REQUIRED_FIELDS = ['mobile', 'password']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.username}'

    def save(self, *args, **kwargs):
        self.username = str(self.username)
        super(CustomUserModel, self).save(*args, **kwargs)

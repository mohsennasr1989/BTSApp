from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import CustomUserModel


@admin.register(CustomUserModel)
class CustomUserAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    search_fields = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    list_filter = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')

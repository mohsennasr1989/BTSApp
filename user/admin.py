from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import CustomUserModel, LocationModel, UserActivityModel


@admin.register(CustomUserModel)
class CustomUserAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    search_fields = (
        'id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    list_filter = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')


@admin.register(LocationModel)
class LocationAdmin(ModelAdmin):
    list_display = ('id', 'country', 'province', 'city')
    search_fields = ('id', 'country', 'province', 'city')
    list_filter = ('id', 'country', 'province', 'city')


@admin.register(UserActivityModel)
class UserActivityAdmin(ModelAdmin):
    list_display = ('id', 'activity')
    search_fields = ('id', 'activity')
    list_filter = ('id', 'activity')

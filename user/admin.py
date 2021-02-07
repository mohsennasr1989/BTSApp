from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from user.models import CustomUserModel, LocationModel, UserActivityModel


@admin.register(CustomUserModel)
class CustomUserAdmin(ImportExportModelAdmin, ModelAdmin):
    model = CustomUserModel
    list_display = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    search_fields = (
        'id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    list_filter = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')
    export_order = ('id', 'first_name', 'last_name', 'username', 'password', 'location', 'activity', 'address', 'phone')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(LocationModel)
class LocationAdmin(ImportExportModelAdmin, ModelAdmin):
    model = LocationModel
    list_display = ('country', 'province', 'city')
    search_fields = ('country', 'province', 'city')
    list_filter = ('country', 'province', 'city')
    export_order = ('id', 'country', 'province', 'city', 'create_date')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]


@admin.register(UserActivityModel)
class UserActivityAdmin(ImportExportModelAdmin, ModelAdmin):
    model = UserActivityModel
    list_display = ('id', 'activity')
    search_fields = ('id', 'activity')
    list_filter = ('id', 'activity')
    export_order = ('id', 'activity')

    def get_import_formats(self):
        """
        Returns available import formats.
        """
        formats = (
            base_formats.CSV,
            base_formats.XLS,
            base_formats.XLSX,
            base_formats.TSV,
            base_formats.ODS,
            base_formats.JSON,
            base_formats.YAML,
            base_formats.HTML,
        )
        return [f for f in formats if f().can_export()]

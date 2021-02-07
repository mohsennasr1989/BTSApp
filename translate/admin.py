from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Dictionary
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats


@admin.register(Dictionary)
class DictionaryAdmin(ImportExportModelAdmin, ModelAdmin):
    model = Dictionary
    list_display = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')
    search_fields = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')
    list_filter = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')
    export_order = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')

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

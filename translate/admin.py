from django.contrib import admin
from .models import Dictionary


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')
    search_fields = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')
    list_filter = ('id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate')

from rest_framework import serializers

from .models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['id', 'item_name', 'fa_translate', 'en_translate', 'ar_translate', 'ru_translate']

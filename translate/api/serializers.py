from rest_framework import serializers

from translate.models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
        read_only_fields = ['id', 'create_date']

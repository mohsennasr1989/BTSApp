from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Dictionary
from .serializers import DictionarySerializer


class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer

    def list(self, request, **kwargs):
        serializer = DictionarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        dictionary = get_object_or_404(self.queryset, pk=pk)
        serializer = DictionarySerializer(dictionary)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], pk=None)
    def get_translate(self, request):
        if request.data['lang'] is not None:
            language = request.data['lang']
            if language == 'fa':
                return self.queryset.get('fa_translate')
            elif language == 'en':
                return self.queryset.get('en_translate')
            elif language == 'ar':
                return self.queryset.get('ar_translate')
            elif language == 'ru':
                return self.queryset.get('ru_translate')

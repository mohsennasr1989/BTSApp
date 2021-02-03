from django.http import HttpResponse
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

    @action(detail=True, methods=['GET'])
    def get_translate(self, request, pk=None):
        serializer = DictionarySerializer(get_object_or_404(self.queryset, pk=pk))
        # if request.['lang'] is not None:
        #     if request.GET.data['lang'] == 'en':
        #         return Response(serializer.data['en_translate'])
        #     elif request.GET.data['lang'] == 'fa':
        #         return Response(serializer.data['fa_translate'])
        return Response(serializer.data['fa_translate'])


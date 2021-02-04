from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from translate.models import Dictionary
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
        if request.query_params.get('lang') is not None:
            lang = request.query_params.get('lang')
            if lang == 'en':
                return Response(serializer.data['en_translate'])
            elif lang == 'fa':
                return Response(serializer.data['fa_translate'])
            elif lang == 'ar':
                return Response(serializer.data['ar_translate'])
            elif lang == 'ru':
                return Response(serializer.data['ru_translate'])

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
            if self.request.query_params.get('lang') in ('fa', 'en', 'ru', 'ar'):
                permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
            if self.request.query_params.get('lang') in ('fa', 'en', 'ru', 'ar'):
                permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


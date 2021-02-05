from rest_framework import serializers

from user.models import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'
        read_only_fields = ['id', 'create_date']

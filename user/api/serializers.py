from django.core.exceptions import ValidationError
from rest_framework import serializers, status
import django.contrib.auth.password_validation as validators
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user.models import CustomUserModel, LocationModel


class CustomUserSerializer(serializers.ModelSerializer):
    # activity_name = serializers.ReadOnlyField(source='activity.__str__')
    # location_name = serializers.ReadOnlyField(source='location.__str__')
    class Meta:
        model = CustomUserModel
        fields = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'first_name', 'last_name',
                  'username', 'password', 'address', 'phone', 'location', 'activity', 'groups',
                  'user_permissions', 'rule', 'login_token', 'firebase_token')
        read_only_fields = ['id', 'last_login', 'date_joined']

        def create(self, validated_data):
            user = CustomUserModel.objects.create(**validated_data)
            return user

        def validate(self, data):
            user = CustomUserModel(**data)
            password = data.get('password')
            errors = dict()
            if CustomUserModel.objects.filter(username=data.get('mobile_number')):
                errors['mobile_number'] = "User with this phone number already exists."
            if data.get('password') != data.get('confirm_password'):
                errors['password_match'] = "Password and Confirm Password do not match!"
            try:
                validators.validate_password(password=password, user=user)
            except ValidationError as e:
                errors['password'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)
            return super(CustomUserSerializer, self).validate(data)

        def update(self, instance, validated_data):
            pass


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ('id', 'country', 'province', 'city')
        read_only_fields = ['id', 'create_date']


class TokenSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.__str__')

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_name', 'created')

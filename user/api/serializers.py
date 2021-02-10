from django.core import exceptions
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from user.models import CustomUserModel, LocationModel
from phonenumber_field import validators as phone_validators


class CustomUserSerializer(serializers.ModelSerializer):
    activity_name = serializers.ReadOnlyField(source='activity.__str__')
    location_name = serializers.ReadOnlyField(source='location.__str__')

    class Meta:
        model = CustomUserModel
        fields = ('id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'first_name', 'last_name',
                  'username', 'password', 'address', 'phone', 'location_name', 'activity_name', 'groups',
                  'user_permissions', 'rule', 'login_token', 'firebase_token')
        read_only_fields = ['id', 'last_login', 'date_joined']

        def create(self, validated_data):
            validated_data['username'] = validated_data['username']
            user = CustomUserModel.objects.create_user(**validated_data)
            return user

        def validate(self, data):
            user = CustomUserModel(**data)
            password = data.get('password')
            errors = dict()
            try:
                validators.validate_password(password=password, user=user)
                if data.get('password') != data.get('confirm_password'):
                    errors['password'] = "Password and Confirm Password do not match!"
                phone_validators.validate_international_phonenumber(data.get('mobile_number'))
                if CustomUserModel.objects.filter(username=data.get('mobile_number')):
                    errors['mobile_number'] = "User with this phone number already exists."
            except exceptions.ValidationError as e:
                errors['validation'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)

            return super(CustomUserSerializer, self).validate(data)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ('id', 'country', 'province', 'city')
        read_only_fields = ['id', 'create_date']

from django.core import exceptions
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from user.models import CustomUserModel
from phonenumber_field import validators as phone_validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'
        read_only_fields = ['id', 'create_date']

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

            return super(UserSerializer, self).validate(data)

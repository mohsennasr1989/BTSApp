from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from user.api.serializers import UserSerializer
from user.models import CustomUserModel


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    try:
        data = request.data
        serializer = UserSerializer(data).validate(data)
        request.session['signup_data'] = serializer

        user = CustomUserModel(first_name=data['first_name'],
                               last_name=data['last_name'],
                               username=data['mobile'],
                               password=data['password'],
                               location=data['location'],
                               activity=data['activity'],
                               address=data['address'],
                               phone=data['phone']
                               )
        user.set_password(data['password'])
        user.save()

    except Exception as e:
        request.session.flush()
        return Response({'status': "Sign up failed.", 'error': str(e)},
                        status=HTTP_400_BAD_REQUEST)
    return Response({'status': "Signup Success"},
                    status=HTTP_200_OK)

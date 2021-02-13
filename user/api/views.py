from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import CustomUserSerializer, TokenSerializer
from ..models import CustomUserModel, UserActivityModel, LocationModel
from rest_framework.authtoken.models import Token


class CustomUserViewSet(ViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer

    @permission_classes((IsAuthenticated,))
    def list(self, request, **kwargs):
        serializer = CustomUserSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes((IsAuthenticated,))
    def retrieve(self, request, pk=None, **kwargs):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    @login_required
    @permission_classes((IsAuthenticated,))
    def get_by_username(self, request):
        if request.query_params.get('user_name') is not None:
            username = request.query_params.get('user_name')
            serializer = CustomUserSerializer(get_object_or_404(self.queryset, username=username))
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    @login_required
    @permission_classes((IsAuthenticated,))
    def get_active_users(self, request):
        users = CustomUserModel.objects.filter(is_active=True)
        serializer = CustomUserSerializer(users, many=True)
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    @login_required
    @permission_classes((IsAuthenticated,))
    def get_by_activity(self, request):
        if request.query_params.get('activity') is not None:
            activity_name = request.query_params.get('activity')
            try:
                activity_id = UserActivityModel.objects.get(activity=activity_name)
            except UserActivityModel.DoesNotExist:
                activity_id = None
            if activity_id is not None:
                queryset = self.queryset.filter(activity=activity_id)
                serializer = CustomUserSerializer(queryset, many=True)
                if serializer.is_valid():
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    @login_required
    @permission_classes((IsAuthenticated,))
    def get_by_province(self, request):
        if request.query_params.get('province') is not None:
            province_name = request.query_params.get('province')
            try:
                location_id = LocationModel.objects.get(province=province_name)
            except LocationModel.DoesNotExist:
                location_id = None
            if location_id is not None:
                queryset = self.queryset.filter(location=location_id)
                serializer = CustomUserSerializer(queryset, many=True)
                if serializer.is_valid():
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    @permission_classes((AllowAny,))
    def signup(self, request):
        try:
            data = request.data
            serializer = CustomUserSerializer(data).validate(data)
            request.session['signup_data'] = serializer

            user = CustomUserModel(first_name=data['first_name'],
                                   last_name=data['last_name'],
                                   username=data['mobile'],
                                   password=data['password'],
                                   location=data['location'],
                                   activity=data['activity'],
                                   address=data['address'],
                                   phone=data['phone'])
            user.set_password(data['password'])
            user.save()
            user.login_token = Token.objects.get_or_create(user=user)
            user.save()

        except Exception as e:
            request.session.flush()
            return Response({'status': "Sign up failed.", 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': "Signup Success"},
                        status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=False, methods=['GET', 'POST'])
    @permission_classes((AllowAny,))
    def login(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                token = Token.objects.get_or_create(user=user, self=self)
                user.login_token = token
                print(token.key)
                user.save()
            else:
                return Response({'status': "Invalid username or password."},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            request.session.flush()
            return Response({'status': "Login failed.", 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': "Login success."},
                        status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=False, methods=['POST'])
    @permission_classes((IsAuthenticated,))
    def update_user(self, request):
        if request.data is not None:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('Request Failed', status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    @permission_classes((IsAdminUser,))
    def get_tokens_list(self, request):
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    @permission_classes((IsAdminUser,))
    def get_token(self, request):
        try:
            user_id = request.GET['user_id']
        except Exception as e:
            request.session.flush()
            return Response({'status': "Request failed.", 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        if user_id is not None:
            try:
                token = Token.objects.get(user=user_id)
            except Exception as e:
                return Response(str(e), status=status.HTTP_404_NOT_FOUND)
            serializer = TokenSerializer(token)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    @permission_classes((IsAdminUser,))
    def update_tokens(self, request):
        is_modified = False
        for user in CustomUserModel.objects.all():
            if user.login_token == "":
                try:
                    token = Token.objects.get(user=user.id)
                except Exception as e:
                    token = Token(user=user)
                user.login_token = token.key
                user.save()
                is_modified = True
        if is_modified:
            users = CustomUserModel.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    @permission_classes((IsAuthenticated,))
    def get_user_by_token(self, request):
        try:
            token_value = request.GET['token']
        except Exception as e:
            request.session.flush()
            return Response({'status': "Request failed.", 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        if token_value is not None:
            try:
                token = Token.objects.get(key=token_value)
            except Exception as e:
                return Response(str(e), status=status.HTTP_404_NOT_FOUND)
            user = CustomUserModel.objects.get(pk=token.user.id)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    @action(detail=False, methods=['GET', 'POST'])
    @permission_classes((IsAuthenticated,))
    def logout(self, request):
        logout(request=request)
        return Response({'status': "Logout success."},
                        status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=False, methods=['GET', 'POST'])
    @permission_classes((IsAuthenticated,))
    def reset_token(self, request):
        user = get_user(request)
        if user is not None:
            try:
                token = Token.objects.get(user=user)
                token.delete()
            except Exception as e:
                token = None
            token = Token.objects.create(user=user)
            user.login_token = token.key
            user.save()
            serializer = CustomUserSerializer(user)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'status': "Invalid username or password."},
                            status=status.HTTP_401_UNAUTHORIZED)

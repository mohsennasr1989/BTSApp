from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from ..models import CustomUserModel, UserActivityModel, LocationModel
from rest_framework.authtoken.models import Token


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer

    @login_required
    @permission_required('user.view', login_url='/user/login')
    def list(self, request, **kwargs):
        serializer = CustomUserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        product_type = get_object_or_404(self.queryset, pk=pk)
        serializer = CustomUserSerializer(product_type)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_by_username(self, request):
        if request.query_params.get('id') is not None:
            username = request.query_params.get('id')
            serializer = CustomUserSerializer(get_object_or_404(self.queryset, username=username))
            return Response(serializer.data)
        return Response(status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def get_active_users(self, request):
        serializer = CustomUserSerializer(get_object_or_404(self.queryset, is_active=True))
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
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
                return Response(serializer.data)
        return Response(status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
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
                return Response(serializer.data)
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
                Token.objects.get_or_create(user=user)
            else:
                return Response({'status': "Invalid username or password."},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            request.session.flush()
            return Response({'status': "Login failed.", 'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': "Login success."},
                        status=status.HTTP_200_OK)

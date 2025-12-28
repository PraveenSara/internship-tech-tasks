from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password


@api_view(['GET'])
def test_api(request):
    return Response({
        "message": "Django REST API is working!",
        "status": "success"
    })

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User created successfully!"})
    return Response(serializer.errors)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username).first()
    
    if not user:
        return Response({"error":"Invalid credentials"}, status=401)
    
    if not check_password(password, user.password):
        return Response({"error":"Invalid credentials"}, status=401)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        "message":"Login successful",
        "access": str(refresh.access_token),
        "refresh": str(refresh)
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_users(request):
    users = User.objects.all().values('id','username','email')
    return Response(list(users))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_users(request):
    if not request.user.is_staff:
        return Response(
            {"error":"Admin access required"},
            status=403
        )
    
    users = User.objects.all().values('id', 'username', 'email')
    return Response(list(users))
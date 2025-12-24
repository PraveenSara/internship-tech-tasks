from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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

@api_view(['POSt'])
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

    if user is None:
        return Response({"error": "User not found"}, status=404)
    
    if not user.check_password(password):
        return Response({"error": "Invalid Password"}, status=401)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_users(request):
    users = User.objects.all().valuse('id','username','email')
    return Response(list(users))
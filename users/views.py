from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('u-index.html')


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer
@api_view(['POST'])
def signup_api(request):

    ser = UserSerializer(data=request.data)

    if ser.is_valid():
        ser.save()

        return Response(
            {"message" : "User created successfully"}
        )

    return Response(ser.errors)

@api_view(['POST'])
def login_api(request):
    uname = request.data.get('username')
    upass = request.data.get('password')

    user = authenticate(
        username=uname,
        password=upass
    )

    if user:
        login(request, user)
        return Response(
            {'message: logined successfully'}
        )
    return Response({
        'message' : 'invalid credentials'
    })

from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response(
        {'user' : str(request.user)}
    )

@api_view(['POST'])
def logout_api(request):
    logout(request)
    return Response(
        {'message ' : 'logged out'}
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])

def staff_dashboard(request):
    if request.user.is_staff:
        return Response(
            {"message" : "welcome to Staff Login"}
        )
    return Response(
        {"message" : "access Denied"}
    )
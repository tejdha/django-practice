from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Workoutserializer
from .models import workouts
# Create your views here.

def base(request):
    return HttpResponse('w-index.html')

def details(request):
    return HttpResponse('hi')

@api_view(['GET'])
def workout_api(request):
    workout = workouts.objects.all()
    serializer = Workoutserializer(workout, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def completed(request):
    workout = workouts.objects.filter(status=True)

    serial = Workoutserializer(workout, many=True)
    return Response(serial.data)

@api_view(['POST'])
def add_api(request):

    work = Workoutserializer(data= request.data)

    if work.is_valid():
        work.save()
        return Response(work.data)
    
    return Response(work.errors)

@api_view(['PUT'])
def update_api(request,id):
    work = workouts.objects.get(id=id)

    ser = Workoutserializer(work, data=request.data)

    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(['DELETE'])
def delete_api(request, id):
    dlt = workouts.objects.get(id=id)

    dlt.delete()
    return Response("workout deleted")


        


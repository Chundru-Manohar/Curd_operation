from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .searilizer import StudentSerializer
# Create your views here.

@api_view(['GET'])  #read
def display(request):
    stud = Student.objects.all()
    ser = StudentSerializer(stud,many=True)
    return Response(ser.data)

@api_view(['POST'])  #send
def post(request):
    ser = StudentSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['POST'])  #update
def update(request,id):
    stud = Student.objects.get(id = id)
    ser = StudentSerializer(instance= stud,data = request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(['DELETE'])  #delete
def delete(request,id):
    stud = Student.objects.get(id = id)
    stud.delete()
    return Response('data delete sucessfully')

@api_view(['GET'])  #GETsingle viw data 
def viewss(request,id):
    stud = Student.objects.get(id = id)
    ser = StudentSerializer(stud)
    return Response(ser.data)

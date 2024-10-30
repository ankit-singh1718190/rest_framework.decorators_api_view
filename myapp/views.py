from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your models here.
@api_view(['GET','POST','PUT','DELETE'])
def GetFuncation(request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    #Post Request
    if request.method=='POST':
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.errors)
    #put Request
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)
    # Delete request
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data deleted'})
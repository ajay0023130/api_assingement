from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
def index(request):
    return HttpResponse("this is first page")


from rest_framework.response import Response    
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def EmpList(request):
    obj = Employee.objects.all()
    sobj = EmployeeSerializer(obj,many=True)
    return Response(sobj.data)


@api_view(['GET'])
def EmpDetails(request,pk):
    obj = Employee.objects.get(id=pk)
    sobj = EmployeeSerializer(obj,many=False)
    return Response(sobj.data)  



@api_view(['POST'])
def EmpCreate(request):
    ser = EmployeeSerializer(data = request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)    
    


@api_view(['POST'])
def EmpUpdate(request,pk):
    emp = Employee.objects.get(id=pk)
    ser = EmployeeSerializer(instance=emp,data = request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)  


@api_view(['DELETE'])
def EmpDelete(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return Response({"status": "success", "data": "Item Deleted"})       
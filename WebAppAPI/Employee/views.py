from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Department, Employess
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
@csrf_exempt
def DepartmentApi(request, id=0):
    if request.method == 'GEt':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)

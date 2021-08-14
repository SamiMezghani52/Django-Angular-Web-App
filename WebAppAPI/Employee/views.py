from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Department, Employess
from .serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

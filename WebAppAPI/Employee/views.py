from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Department, Employess
from .serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def DepartmentApi(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully ...", safe=False)
        return JsonResponse("Failed to add...", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully ...", safe=False)
        return JsonResponse("Failed to update ...")

    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Item deleted successfully ...", safe=False)

@csrf_exempt
def EmployeeAPI (request, id=0):
    if request.method == 'GET':
        employee = Employess.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee created successfully...", safe=False)
        return JsonResponse("Failed to create the employee ...", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employess.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee updated successfully...", safe=False)
        return JsonResponse("Failed to update Employee ...", safe=False)
    
    elif request.method == 'DELETE':
        employee = Employess.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Employee deleted successfully ...", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file) 

    return JsonResponse(file_name, safe=False)

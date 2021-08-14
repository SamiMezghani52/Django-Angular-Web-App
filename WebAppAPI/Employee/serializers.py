from rest_framework import serializers 
from .models import Department, Employess

class DepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'DepartmentId',
            'DepartmentName'
        )

class EmployeeSerializer (serializers.ModelSerializer):
    class Meta :
        model = Employess
        fields = (
            'EmployeeId',
            'EmployeeName',
            'Department',
            'DateOfJoining',
            'PhotoFileName'
        )
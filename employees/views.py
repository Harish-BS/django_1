from django.shortcuts import render
from .models import employee
from .serializers import employeesSerializers
from django.http import JsonResponse

def employee_list(request):
    Employees = employee.objects.all()
    serializer = employeesSerializers(Employees, many = True)
    return JsonResponse(serializer.data, safe = False)
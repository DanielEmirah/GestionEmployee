from django.shortcuts import render, get_object_or_404
from .models import Employee


def index(request):
    employees = Employee.objects.all()
    context = {
        "employees" : employees
    }
    return render(request, "crew/list.html", context)


def details(request, id):
    employee = get_object_or_404(Employee, pk=id)
    context = {
        "employee" : employee
    }
    return render(request, "crew/details.html", context)
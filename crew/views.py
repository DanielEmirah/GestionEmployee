from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm


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

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crew:list_employee")
    form = EmployeeForm()
    return render(request, "crew/formulaire.html", {"form": form})
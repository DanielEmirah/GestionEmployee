from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee

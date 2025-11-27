from django.urls import path
from . import views

app_name = "crew"

urlpatterns = [
    path('', views.list_employee, name="list_employee"),
]

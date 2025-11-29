from django.urls import path
from . import views

app_name = "crew"

urlpatterns = [
    path('', views.index, name="list_employee"),
    path('crew/create/', views.create_employee, name="create_employee"),
    path('crew/<int:id>/', views.details, name="details"),
]

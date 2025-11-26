from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    phone = models.CharField(max_length=13)
    poste = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
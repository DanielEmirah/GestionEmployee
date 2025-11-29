from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'mail' : forms.EmailInput(attrs={'placeholder': 'exemple@email.com'}),
            'phone' : forms.TextInput(attrs={'placeholder': '+261...'}),
            'poste' : forms.TextInput(attrs={'placeholder': 'Assistan de projet'}),
            'salary' : forms.NumberInput(attrs={'placeholder': 'Salaire en dollars'}),
        }
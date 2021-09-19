from django import forms
from .models import Employer
from .models import Departement

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'

from django import forms
from first_app.models import Patient

class FormName(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

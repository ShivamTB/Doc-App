from django import forms
from first_app.models import Patient, BirthHistory, Visit

class FormName(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class History(forms.ModelForm):
    class Meta:
        model = BirthHistory
        fields = '__all__'

class CheckUP(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

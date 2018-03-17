from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .filters import PatientFilter
from .models import Patient
# Create your views here.

def index(request):
    my_dict = {'insert_me' : "Hello I am from first_app/index.html"}
    return render(request,'first_app/index.html',context=my_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS")
            print("NAME: " + form.cleaned_data['name'])


    return render(request, 'first_app/form_page.html',{'form':form})

def search(request):
    patient_list = Patient.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patient_list)
    return render(request, 'first_app/patient_list.html', {'filter': patient_filter})

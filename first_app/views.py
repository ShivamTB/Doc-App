from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .filters import PatientFilter
from .models import Patient
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.

def index(request):
    patient_list = Patient.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patient_list)
    my_dict = {'insert_me' : "Hello I am from first_app/index.html",'filter': patient_filter}
    return render(request,'first_app/index.html',context=my_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING
            print("VALIDATION SUCCESS")


    return render(request, 'first_app/form_page.html',{'form':form})


def search(request):
    patient_list = Patient.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patient_list)
    return render(request, 'first_app/index.html', {'filter': patient_filter})

def pat_list(request):
    patients = Patient.objects.all()
    return render(request, 'first_app/pat_list.html', {'patients': patients})

def save_patient_form(request, form, template_name):
    data = dict()

    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
        patients = Patient.objects.all()
        data['html_patient_list'] = render_to_string('first_app/includes/partial_patient_list.html', {
            'patients': patients
        })
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def patient_create(request):

    if request.method == 'POST':
        form = forms.FormName(request.POST)
    else:
        form = forms.FormName()
    return save_patient_form(request, form, 'first_app/includes/partial_patients_create.html')

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = forms.FormName(request.POST, instance=patient)
    else:
        form = forms.FormName(instance=patient)
    return save_patient_form(request, form, 'first_app/includes/partial_patient_update.html')

def patient_fetch(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    return JsonResponse(serializers.serialize('json', [ patient, ]), safe = False)

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    data = dict()
    if request.method == 'POST':
        patient.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        patients = Patient.objects.all()
        data['html_patient_list'] = render_to_string('first_app/includes/partial_patient_list.html', {
            'patients': patients
        })
    else:
        context = {'patient': patient}
        data['html_form'] = render_to_string('first_app/includes/partial_patient_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

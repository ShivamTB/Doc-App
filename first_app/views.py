from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .filters import PatientFilter
from .models import Patient, Visit, BirthHistory
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from datetime import datetime
import json


# Create your views here.

def index(request):
    patient_list = Patient.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=patient_list)
    my_dict = {'filter': patient_filter}
    return render(request,'first_app/index.html',context=my_dict)

def form_name_view(request):
    form = forms.CheckUP()

    if request.method == 'POST':
        form = forms.CheckUP(request.POST)

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

def save_history_form(request, form, template_name):
    data = dict()

    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def history_create(request):

    if request.method == 'POST':
        form = forms.History(request.POST)
    else:
        form = forms.History()
    return save_history_form(request, form, 'first_app/includes/partial_history_create.html')

def history_update(request, pk):
    history = get_object_or_404(Visit, pk=pk)
    if request.method == 'POST':
        form = forms.History(request.POST, instance=history)
    else:
        form = forms.History(instance=history)
    return save_history_form(request, form, 'first_app/includes/partial_history_update.html')

def save_visit_form(request, form, template_name):
    data = dict()

    if form.is_valid():
        form.save()
        data['form_is_valid'] = True
    else:
        data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def visit_create(request):

    if request.method == 'POST':
        form = forms.CheckUP(request.POST)
    else:
        form = forms.CheckUP()
    return save_visit_form(request, form, 'first_app/includes/partial_visit_create.html')

def visit_update(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    last_visit = last_visit(visit.patient.pk)
    if request.method == 'POST':
        form = forms.CheckUP(request.POST, instance=patient)
    else:
        form = forms.CheckUP(instance=patient)
    return save_visit_form(request, form, 'first_app/includes/partial_visit_update.html')

def visit_delete(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    data = dict()
    if request.method == 'POST':
        patient.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'patient': patient}
        data['html_form'] = render_to_string('first_app/includes/partial_visit_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def last_visit(pk, ppk):
    while(pk>0):
        pk -= 1
        visit = get_object_or_404(Visit, pk=pk)
        if (visit.patient.pk == ppk):
            return pk



def patient_fetch(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient = serializers.serialize('json', [patient])
    struct = json.loads(patient)
    patient = json.dumps(struct[0])
    return JsonResponse(patient, safe=False)

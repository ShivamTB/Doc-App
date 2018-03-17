from first_app.models import Patient
import django_filters

class PatientFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    sur_name = django_filters.CharFilter(lookup_expr='icontains')
    father_name = django_filters.CharFilter(lookup_expr='icontains')
    mother_name = django_filters.CharFilter(lookup_expr='icontains')
    first_name.label_tag = 'First Name'
    class Meta:
        model = Patient
        fields = ['pat_number', 'first_name', 'sur_name','dob','father_name','mother_name']


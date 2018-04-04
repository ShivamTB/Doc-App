from first_app.models import Patient
import django_filters

class PatientFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label = 'First Name')
    sur_name = django_filters.CharFilter(lookup_expr='icontains', label = 'Sur Name')
    father_name = django_filters.CharFilter(lookup_expr='icontains', label = "Father's Name")
    mother_name = django_filters.CharFilter(lookup_expr='icontains', label = "Mother's Name")
    class Meta:
        model = Patient
        fields = ['pat_number', 'first_name', 'sur_name','dob','father_name','mother_name']

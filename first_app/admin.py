from django.contrib import admin

# Register your models here.
from first_app.models import Patient, UnregForm3C, Form3C, Generic

admin.site.register(Patient)
admin.site.register(Form3C)
admin.site.register(UnregForm3C)
admin.site.register(Generic)

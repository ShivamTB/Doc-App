from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=32)
    sur_name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.first_name

class Patient(models.Model):
    pat_number = models.PositiveSmallIntegerField(default = 0)
    first_name = models.CharField(max_length=32, default = "NOTFOUND")
    sur_name = models.CharField(max_length=32, blank=True)
    status = models.BooleanField(default=True)
    dob = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    sex_choices = (('M', 'Male'),('F','Female'))
    sex = models.CharField(max_length = 1, choices = sex_choices, blank=True, null=True)
    blood = models.CharField(max_length=3, blank=True, null=True)
    registration_date = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    father_name = models.CharField(max_length=32, blank=True, null=True)
    father_blood = models.CharField(max_length=3, blank=True, null=True)
    father_occupation = models.CharField(max_length=32, blank=True, null=True)
    father_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    father_email = models.EmailField(max_length=254, blank=True, null=True)

    mother_name = models.CharField(max_length=32, blank=True, null=True)
    mother_blood = models.CharField(max_length=3, blank=True, null=True)
    mother_occupation = models.CharField(max_length=32, blank=True, null=True)
    mother_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    mother_email = models.EmailField(max_length=254, blank=True, null=True)

    address = models.TextField(blank=True, null=True)
    city =  models.CharField(max_length = 32, blank=True, null=True)
    state = models.CharField(max_length = 32, blank=True, null=True)
    pin_code = models.CharField(max_length = 6, blank=True, null=True)

    pob = models.CharField(max_length = 32, blank=True, null=True)
    delivery_doctor = models.CharField(max_length = 32, blank=True, null=True)

    birth_weight = models.DecimalField(max_digits=6, decimal_places=2,default=0, blank=True, null=True)
    birth_height = models.DecimalField(max_digits=3, decimal_places=1,default=0, blank=True, null=True)
    birth_headcm = models.DecimalField(max_digits=3, decimal_places=1,default=0, blank=True, null=True)

    last_weight = models.DecimalField(max_digits=6, decimal_places=2,default=0, blank=True, null=True)
    last_height = models.DecimalField(max_digits=4, decimal_places=1,default=0, blank=True, null=True)
    last_headcm = models.DecimalField(max_digits=4, decimal_places=1,default=0, blank=True, null=True)
    last_date = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    last_note = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.first_name

class Form3C(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    pat = models.ForeignKey(Patient)
    name = models.CharField(max_length=64)
    purpose = models.CharField(max_length=64)
    charges = models.DecimalField(max_digits = 5, decimal_places=0)

    def __str__(self):
        return str(self.date)

class UnregForm3C(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=64)
    purpose = models.CharField(max_length=64)
    charges = models.DecimalField(max_digits = 5, decimal_places=0)

    def __str__(self):
        return str(self.date)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length = 32)
    notes = models.TextField

    def __str__(self):
        return str(self.date)

class Vaccine(models.Model):
    vac_types = (('R', 'Regular'),('S','Special'))
    vac_type = models.CharField(max_length = 1, choices = vac_types)
    name = models.CharField(max_length=16)
    charges = models.DecimalField(max_digits = 5, decimal_places=0)
    notes = models.TextField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    vaccine = models.ForeignKey(Vaccine)
    company = models.CharField(max_length=16)
    batch = models.CharField(max_length=16)
    quantity = models.PositiveSmallIntegerField()
    expiry = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.batch

class Vaccination(models.Model):
    patient = models.ForeignKey(Patient)
    vaccine = models.ForeignKey(Vaccine)
    inventory = models.ForeignKey(Inventory)
    vac_scheduled_date = models.DateField(auto_now=False, auto_now_add=False)
    vac_actual_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.vac_actual_date)

class Visit(models.Model):
    patient = models.ForeignKey(Patient)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    height = models.DecimalField(max_digits=4, decimal_places=1,default=0)
    headcm = models.DecimalField(max_digits=4, decimal_places=1,default=0)
    bp_systolic = models.DecimalField(max_digits = 3, decimal_places=0)
    bp_diastolic = models.DecimalField(max_digits = 3, decimal_places=0)
    charges = models.DecimalField(max_digits = 5, decimal_places=0)
    vaccination_charges = models.DecimalField(max_digits = 5, decimal_places=0)
    next_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)

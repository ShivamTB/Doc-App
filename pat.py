import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from decimal import Decimal
import django
django.setup()

import csv
from first_app.models import Patient
from datetime import datetime


input_file = csv.DictReader(open("patients.txt"))

for row in input_file:
    if (row["PAT_STATUS"] == "Y"):
        status = True
    else:
        status = False
    print(row)
    patient = Patient.objects.get_or_create(
                pat_number = row["PAT_NO"],
                first_name = row["PAT_NAME"],
                sur_name = row["PAT_SURNM"],
                status = status,
                dob = datetime.strptime(row["PAT_DOB"], '%d-%m-%Y %H:%M:%S'),
                sex = row["PAT_SEX"],
                blood = row["PAT_BLOOD"],

                father_name = row["PAT_FATHER"],
                father_blood = row["pat_mblood"],
                father_occupation = row["PAT_FOCC"],
                father_phone_number = row["PAT_TEL1"],
                father_email = row["PAT_EMAIL"],

                mother_name = row["PAT_MOTHER"],
                mother_blood = row["pat_mblood"],
                mother_occupation = row["PAT_MOCC"],
                mother_phone_number = row["PAT_TEL2"],
                mother_email = row["PAT_EMAIL"],


                address = row["PAT_ADDR1"],
                city =  row["PAT_ADDR3"],
                state = row["PAT_ADDR3"],
                pin_code = row["PAT_ADDR4"],

                pob = row["PAT_POB"],
                delivery_doctor = row["PAT_DELDOC"],

                birth_weight = row["PAT_BRTHWT"],
                birth_height = row["PAT_BRTHLN"],
                birth_headcm = row["PAT_BRTHCM"],
                last_weight = row["PAT_LSTWT"],
                last_height = row["PAT_LSTHT"],
                last_headcm = row["PAT_LSTHC"],
                last_date = datetime.strptime(row["PAT_LSTDT"], '%d-%m-%Y %H:%M:%S'),
                last_note = row["PAT_LSTNOTE"])[0]
    patient.save()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from decimal import Decimal
import django
django.setup()

import csv
from first_app.models import Form3C, Patient
from datetime import datetime


input_file = csv.DictReader(open("formc.txt"))

for row in input_file:
    u3c = Form3C.objects.get_or_create(
        date = datetime.strptime(row["FR_DATE"], '%d-%m-%Y %H:%M:%S'),
        pat = Patient.objects.get(pat_number=row["FR_PAT"]),
        name = row["FR_NAME"],
        purpose = row["FR_PURPOSE"],
        charges = row["FR_CHARGES"]
        )[0]
    u3c.save()

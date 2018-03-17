import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from decimal import Decimal
import django
django.setup()

import csv
from first_app.models import UnregForm3C
from datetime import datetime


input_file = csv.DictReader(open("unregform3c.txt"))

for row in input_file:
    u3c = UnregForm3C.objects.get_or_create(
        date = datetime.strptime(row["U3C_DATE"], '%d-%m-%Y %H:%M:%S'),
        name = row["U3C_NAME"],
        purpose = row["U3C_PURPOSE"],
        charges = row["U3C_AMOUNT"]
        )[0]
    u3c.save()

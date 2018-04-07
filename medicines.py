import os
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from decimal import Decimal
import django
django.setup()

import csv
from first_app.models import Generic
from datetime import datetime


access_token = ''

for i in range(1,3):
    print(i)
    url = 'http://www.healthos.co/api/v1/medicines/generics?page='+str(i)+'&size=30'
    r = requests.get(url, headers={
                            "Authorization": "Bearer " + access_token
                            }).json()
    print(r)

    gen = Generic.objects.get_or_create(
        name = r[i-1]["name"],
        side_effects = r[i-1]["side_effects"],
        )[0]
    u3c.save()

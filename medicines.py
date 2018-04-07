import os
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
from decimal import Decimal
import django
django.setup()

import csv
from first_app.models import Generic
from datetime import datetime


access_token = '4962792aef98d3eedae354677082e3bc095b5fec3e283fa8e4012a0a46d7e21e'

for i in range(12,13):
    print(i)
    #url = 'http://www.healthos.co/api/v1/medicines/generics?page='+str(i)+'&size=25'
    url = 'http://www.healthos.co/api/v1/medicines/generics?page=40&size=25'
    response = requests.get(url, headers={
                            "Authorization": "Bearer " + access_token
                            })
    print(response.headers)
    r = response.json()
    for j in r:
        gen = Generic.objects.get_or_create(
            name = j["name"],
            side_effects = j["side_effects"],
            )[0]
        gen.save()

"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from first_app import views

urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^first_app/',include('first_app.urls')),
    url(r'^formpage/',views.form_name_view,name='form_name'),
    url(r'^formpagejav/',views.pat_list, name='pat_list'),
    url(r'^patient/create/$', views.patient_create, name='patient_create'),
    url(r'^patient/(?P<pk>\d+)/update/$', views.patient_update, name='patient_update'),
    url(r'^history/create/$', views.history_create, name='history_create'),
    url(r'^history/(?P<pk>\d+)/update/$', views.history_update, name='history_update'),
    url(r'^patient/(?P<pk>\d+)/delete/$', views.patient_delete, name='patient_delete'),
    url(r'^patient/(?P<pk>\d+)/fetch/$', views.patient_fetch, name='patient_fetch'),
    url(r'^visit/create/$', views.visit_create, name='visit_create'),
    url(r'^visit/(?P<pk>\d+)/update/$', views.visit_update, name='visit_update'),
    url(r'^visit/(?P<pk>\d+)/delete/$', views.visit_delete, name='visit_delete'),
    url(r'^admin/', admin.site.urls),
]

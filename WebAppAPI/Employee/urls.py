from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department/$', views.DepartmentApi),
    url(r'^department/([0-9]+)$', views.DepartmentApi),

    url(r'^employee/$', views.EmployeeAPI),
    url(r'^employee/([0-9]+)$', views.EmployeeAPI),

    url(r'^SaveFile/$', views.SaveFile)
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^department/$', views.DepartmentApi),
    url(r'^department/([0-9]+)$', views.DepartmentApi),
    url(r'êmployee/$', views.EmployeeAPI),
    url(r'employee/([0-9]+)$', views.EmployeeAPI)
]

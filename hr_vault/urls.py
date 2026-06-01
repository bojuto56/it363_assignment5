from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_employee_record, name="add_employee"),
    path("records/", views.employee_list, name="employee_list"),
]
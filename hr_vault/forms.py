from django import forms
from .models import EmployeeRecord


class EmployeeRecordForm(forms.ModelForm):
    class Meta:
        model = EmployeeRecord
        fields = [
            "employee_name",
            "department",
            "bank_account_number",
            "annual_salary",
        ]
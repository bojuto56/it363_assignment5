from django.contrib import admin
from .models import EmployeeRecord


@admin.register(EmployeeRecord)
class EmployeeRecordAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "department", "annual_salary", "added_by", "created_at")
    search_fields = ("employee_name", "department")
    readonly_fields = ("created_at",)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeRecordForm
from .models import EmployeeRecord


@login_required
def add_employee_record(request):
    if request.method == "POST":
        form = EmployeeRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.added_by = request.user
            record.save()
            return redirect("employee_list")
    else:
        form = EmployeeRecordForm()

    return render(request, "hr_vault/add_employee.html", {"form": form})


@login_required
def employee_list(request):
    records = EmployeeRecord.objects.all()
    return render(request, "hr_vault/employee_list.html", {"records": records})
from django.contrib import admin
from .models import Employee, EmployeeSeniority, Seniority


admin.site.register(Employee)
admin.site.register(EmployeeSeniority)
admin.site.register(Seniority)

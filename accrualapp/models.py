from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField(unique=True, primary_key=True)
    password = models.CharField(max_length=32)
    points_accrued = models.FloatField(default=0)
    points_used = models.FloatField(default=0)

    def __str__(self):
        return "Employee " + str(self.emp_id)


class EmployeeSeniority(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    seniority = models.CharField(max_length=1)

    def __str__(self):
        return "ID " + str(self.employee.emp_id) + " " + self.seniority


class Seniority(models.Model):
    seniority = models.CharField(max_length=1)
    points_per_month = models.IntegerField()

    def __str__(self):
        return self.seniority

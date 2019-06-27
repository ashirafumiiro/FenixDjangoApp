from django.core.management.base import BaseCommand, CommandError
from accrualapp.models import *
from django.utils import timezone
from dateutil import relativedelta
import datetime


class Command(BaseCommand):
    help = 'Perform monthly increment'

    def handle(self, *args, **options):
        employees = Employee.objects.all()
        for employee in employees:
            additional_points = 0
            seniorities = EmployeeSeniority.objects.filter(employee__emp_id=employee.emp_id)
            for seniority in seniorities:
                points_per_month = Seniority.objects.get(seniority=seniority.seniority).points_per_month
                multiplier = self.get_tenure_multiplier(seniority.start_date)
                additional_points += points_per_month * multiplier

            employee.points_accrued += additional_points
            employee.save()
            self.stdout.write("Employee: " + str(employee.emp_id)+" Points added: " + str(additional_points))

    def get_tenure_multiplier(self, start_date):
        current_date = datetime.datetime.now()
        diff = relativedelta.relativedelta(current_date, start_date)
        years = diff.years
        multiplier = 1.0  # for less that 2 years
        if 2 <= years < 4:
            multiplier = 125/100.0
        elif years >= 4:
            multiplier = 150/100.0

        return multiplier

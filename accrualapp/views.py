from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Employee


def index(request):
    if 'employee_id' not in request.session:  # user not logged in
        return HttpResponseRedirect(reverse('accrualapp:login') + "?redirect=true")

    employee = get_object_or_404(Employee, pk=request.session['employee_id'])
    context = {'employee': employee, 'balance_points': employee.points_accrued - employee.points_used}
    return render(request, 'accrualapp/index.html', context)


def login(request):
    if 'employee_id' in request.session:  # user logged in
        return HttpResponseRedirect(reverse('accrualapp:index'))

    if request.method == 'POST':
        try:
            employee = Employee.objects.get(pk=request.POST['id'], password=request.POST['password'])
            request.session['employee_id'] = employee.emp_id
            return HttpResponseRedirect(reverse('accrualapp:index'))
        except Employee.DoesNotExist:
            return render(request, 'accrualapp/login.html', {'error': "Invalid ID or password"})

    error = ''
    if 'redirect' in request.GET:
        error = 'You must Login first'
    return render(request, 'accrualapp/login.html', {'error': error})


def withdraw(request):
    error = ''
    if 'employee_id' not in request.session:  # user not logged in
        return HttpResponseRedirect(reverse('accrualapp:login') + "?redirect=true")

    employee = get_object_or_404(Employee, pk=request.session['employee_id'])
    balance_points = employee.points_accrued - employee.points_used
    if request.method == 'POST':
        if float(request.POST['points']) > balance_points:
            error = 'Insufficient Points'
        elif request.POST['password'] != employee.password:  # invalid Password
            error = 'Invalid Password'
        else:
            employee.points_used += float(request.POST['points'])  # increment the used points by those requested
            employee.save()
            return HttpResponseRedirect(reverse('accrualapp:index'))
    return render(request, 'accrualapp/withdraw.html', {'error': error, 'balance_points': balance_points})


def logout(request):
    if 'employee_id' in request.session:
        del request.session['employee_id']
    return HttpResponseRedirect(reverse('accrualapp:login'))

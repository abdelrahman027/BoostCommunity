from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from chartjs.views.lines import BaseLineChartView
from chartjs.views.pie import HighChartPieView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import random
from .forms import TaskDeliverableForm
from .forms import TasksForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, JobTitle, Employee, Status, Task, TaskProgress, Performance, Badge, Salesman, Trainer, Course, SalesmanCourseAssignment, TrainerCourseAssignment, EmployeeBadge, Meeting, TaskQualityRating, EmployeeSkill, TaskDeliverable
from django.db.models import Sum
from django.utils import timezone
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('employee_profile')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pages/login.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']

        if form.is_valid():
            user = form.save()
            # Print registered user
            print(user)
            print(form.cleaned_data)
            # Create an associated Employee object for the user

            Employee.objects.create(
                user=user, FirstName=firstname, LastName=lastname,  Email=email)

            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {
                             username}! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'pages/sign_up.html', {'form': form})


def index(request):
    x = {'name': 'lovely gemy'}
    return render(request, 'pages/index.html', x)


def dashboard(request):
    # Random data for demonstration
    task_progress = random.randint(0, 100)
    target_profit = random.randint(10000, 50000)
    achieved_percentage = random.randint(0, 100)
    top_employees = [{'name': f'Employee {i}',
                      'points': random.randint(50, 100)} for i in range(1, 6)]
    public_courses = [{'name': f'Course {i}', 'revenue': random.randint(
        5000, 20000), 'trainer': f'Trainer {i}'} for i in range(1, 6)]
    departments_data = [{'department': f'Department {i}', 'progress': random.randint(
        0, 100), 'employees': random.randint(5, 20)} for i in range(1, 6)]
    low_performance_employees = [{'name': f'Employee {
        i}', 'points': random.randint(0, 49)} for i in range(1, 6)]

    context = {
        'task_progress': task_progress,
        'target_profit': target_profit,
        'achieved_percentage': achieved_percentage,
        'top_employees': top_employees,
        'public_courses': public_courses,
        'departments_data': departments_data,
        'low_performance_employees': low_performance_employees,
    }
    return render(request, 'pages/dashboard.html', context)


@login_required
# views.py
@login_required
def employee_profile(request):
    # employee = Employee.objects.get(user=request.user)
    employee = get_object_or_404(Employee, user=request.user)
    tasks = Task.objects.filter(Employee=employee)

    # Get the current month
    current_month = timezone.now().month

    # Get the current month performance for the employee
    current_month_performance = Performance.objects.filter(
        Employee=employee, created_at__month=current_month).first()

    # Get employee badges
    badges = EmployeeBadge.objects.filter(Employee=employee)

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        deliverable_form = TaskDeliverableForm(
            request.POST, request.FILES, task_id=task_id)

        if deliverable_form.is_valid():
            task_deliverable = deliverable_form.save(commit=False)
            task_deliverable.Task = Task.objects.get(pk=task_id)
            task_deliverable.save()
    else:
        deliverable_form = TaskDeliverableForm()

    tasks_form = TasksForm()
    if request.method == 'POST':
        tasks_form = TasksForm(request.POST)
        print(request.POST)
        if tasks_form.is_valid():
            tasks_form.save()
            return redirect('employee_profile')

    context = {
        'employee': employee,
        'tasks': tasks,
        'deliverable_form': deliverable_form,
        'current_month_performance': current_month_performance,
        'badges': badges,
        'task_form': tasks_form,
    }

    return render(request, 'pages/employee_profile.html', context)


def trainer(request):
    trainers_list = Trainer.objects.all()
    employee = get_object_or_404(Employee, user=request.user)

    context = {
        'trainers': trainers_list,
        'employee': employee,
    }

    return render(request, 'pages/trainers.html', context)


def employee(request):
    employee_list = Employee.objects.all()
    employee = get_object_or_404(Employee, user=request.user)

    context = {
        'employees': employee_list,
        'employee': employee,
    }

    return render(request, 'pages/employees.html', context)


def course(request):
    courses_list = Course.objects.all()
    employee = get_object_or_404(Employee, user=request.user)

    context = {
        'courses': courses_list,
        'employee': employee,
    }
    return render(request, 'pages/courses.html', context)


def assign_deliverable(request, task_id):
    if request.method == 'POST':
        # Handle form submission, save deliverable, and update task status
        task = Task.objects.get(pk=task_id)
        deliverable_name = request.POST.get('deliverable_name')
        deliverable_file = request.FILES.get('deliverable_file')

        # Create a new deliverable
        deliverable = TaskDeliverable.objects.create(
            Task=task,
            DeliverableName=deliverable_name,
            DeliverableFile=deliverable_file
        )

        # Update task status to completed
        task.Status = Status.objects.get(StatusName='Completed')
        task.save()

    return redirect('employee_profile')

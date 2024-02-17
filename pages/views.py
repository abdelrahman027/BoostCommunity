import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from chartjs.views.lines import BaseLineChartView
from chartjs.views.pie import HighChartPieView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import random
from .forms import TaskDeliverableForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, JobTitle, Employee, Status, Task, TaskProgress, Performance, Badge, Salesman, Trainer, Course, SalesmanCourseAssignment, TrainerCourseAssignment, EmployeeBadge, Meeting, TaskQualityRating, EmployeeSkill, TaskDeliverable, Client
from django.db.models import Sum, Q
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # SENDING EMAIL LOGIC @@@@@@@
            # subject = f'Welcome {username}'
            # message = f"you logged in to Boost community as {username}"
            # send_mail(
            #     subject,
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     ['abdelrahmansaad027@gmail.com'],
            #     fail_silently=False
            # )
            return redirect('employee_profile')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pages/login.html')

# Multi form register///////////////////

# step1 email,username


def register_username_email(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_email = request.POST['email']
        request.session["username"] = entered_username
        request.session["email"] = entered_email
        return redirect('register-password')
    return render(request, 'pages/register-email-username.html')

# step2 password ,confirm password


def register_password(request):
    if request.method == 'POST':
        entered_password1 = request.POST['password1']
        entered_password2 = request.POST['password2']
        request.session["password1"] = entered_password1
        request.session["password2"] = entered_password2
        return redirect('register')
    return render(request, 'pages/register-password.html')

# Multi form register////////////////////


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
    context = {
        'form': form,
        "username": request.session['username'],
        "password1": request.session['password1'],
        "password2": request.session['password2'],
        "email": request.session['email'],
    }
    return render(request, 'pages/sign_up.html', context)


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
    completed_tasks = Task.objects.filter(Employee=employee, Status=1)
    overdue_tasks = Task.objects.filter(Employee=employee, Status=3)
    inprogress_tasks = Task.objects.filter(Employee=employee, Status=2)
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

    if request.method == 'POST':
        taskname = request.POST.get('TaskName', False)
        Task.objects.create(TaskName=taskname, Employee=employee)
        print(employee)
        return redirect('employee_profile')

    context = {
        'employee': employee,
        'tasks': tasks,
        'deliverable_form': deliverable_form,
        'current_month_performance': current_month_performance,
        'badges': badges,
        'completed_tasks': completed_tasks,
        'inprogress_tasks': inprogress_tasks,
        'overdue_tasks': overdue_tasks,
    }

    return render(request, 'pages/employee_profile.html', context)


def trainer(request):

    employee = get_object_or_404(Employee, user=request.user)
    if 'q' in request.GET:
        q = request.GET['q']
        trainers_list = Trainer.objects.filter(
            Q(FirstName__icontains=q) | Q(LastName__icontains=q))
        print(q)
    else:
        trainers_list = Trainer.objects.all()
        # print(list(Trainer.objects.values()))
    context = {
        'trainers': trainers_list,
        'employee': employee,
        'trainer_json': json.dumps(list(Trainer.objects.values()))
    }

    return render(request, 'pages/trainers.html', context)


def employee(request):
    employee = get_object_or_404(Employee, user=request.user)
    employee_json = json.dumps(
        list(Employee.objects.values()), indent=4, sort_keys=True, default=str),

    if 'q' in request.GET:
        q = request.GET['q']
        employee_list = Employee.objects.filter(
            Q(FirstName__icontains=q) | Q(LastName__icontains=q))
    else:
        employee_list = Employee.objects.all()
        print(employee_json)

    context = {
        'employees': employee_list,
        'employee': employee,
        'employee_json': employee_json
    }

    return render(request, 'pages/employees.html', context)


def course(request):
    employee = get_object_or_404(Employee, user=request.user)
    course_json = json.dumps(
        list(Course.objects.values()), default=str),

    if 'q' in request.GET:
        q = request.GET['q']
        courses_list = Course.objects.filter(CourseName__icontains=q)
        print(q)
    else:
        courses_list = Course.objects.all()

    context = {
        'courses': courses_list,
        'employee': employee,
        'course_json': course_json
    }
    return render(request, 'pages/courses.html', context)


def client(request):
    employee = get_object_or_404(Employee, user=request.user)
    # client_json = json.dumps(list(Client.objects.values())),

    if 'q' in request.GET:
        q = request.GET['q']
        clients_list = Client.objects.filter(
            Q(FirstName__icontains=q) | Q(LastName__icontains=q))
        print(q)
    else:
        clients_list = Client.objects.all()

    context = {
        'clients': clients_list,
        'employee': employee,
        'client_json': json.dumps(list(Client.objects.values())),

    }
    return render(request, 'pages/clients.html', context)


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


def reporting(request):
    employee = get_object_or_404(Employee, user=request.user)

    context = {
        'employee': employee,
    }
    return render(request, 'pages/reporting.html', context)


def employees_tracking(request):
    employee = get_object_or_404(Employee, user=request.user)
    if 'qe' in request.GET:
        qe = request.GET['qe']
        employee_list = Employee.objects.filter(
            Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    else:
        employee_list = Employee.objects.all()

    context = {
        'employee': employee,
        'employees': employee_list,
    }
    return render(request, 'pages/task_tracking.html', context)


def employees_tracking_detail(request, id):
    employee = get_object_or_404(Employee, user=request.user)
    selected_employee = Employee.objects.get(pk=id)
    if 'qe' in request.GET:
        qe = request.GET['qe']
        employee_list = Employee.objects.filter(
            Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    else:
        employee_list = Employee.objects.all()
        # print(selected_employee.Task_set.all())

    context = {
        'employee': employee,
        'selected_employee': selected_employee,
        'employees': employee_list,
        'id': id

    }
    return render(request, 'pages/task_tracking_detail.html', context)

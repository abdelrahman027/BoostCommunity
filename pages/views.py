import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
# from chartjs.views.lines import BaseLineChartView
# from chartjs.views.pie import HighChartPieView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import random
from .forms import TaskDeliverableForm ,CreateActivityForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, JobTitle, Employee, Status, Task, TaskProgress, Performance, Badge, Salesman, Trainer, Course, SalesmanCourseAssignment, TrainerCourseAssignment, EmployeeBadge, Meeting, TaskQualityRating, EmployeeSkill, TaskDeliverable, Client,Activity
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
        if len(taskname) > 0:
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


@login_required
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


@login_required
def employee(request):
    employee = get_object_or_404(Employee, user=request.user)

    if 'q' in request.GET:
        q = request.GET['q']
        employee_list = Employee.objects.filter(
            Q(FirstName__icontains=q) | Q(LastName__icontains=q))
    else:
        employee_list = Employee.objects.all()

    context = {
        'employees': employee_list,
        'employee': employee,
        'employee_json': json.dumps(list(Employee.objects.values()), sort_keys=True, default=str)
    }

    return render(request, 'pages/employees.html', context)


@login_required
def course(request):
    employee = get_object_or_404(Employee, user=request.user)
    # course_json = json.dumps(
    #     list(Course.objects.values()), default=str),

    if 'q' in request.GET:
        q = request.GET['q']
        courses_list = Course.objects.filter(CourseName__icontains=q)
        print(q)
    else:
        courses_list = Course.objects.all()

    context = {
        'courses': courses_list,
        'employee': employee,
        'course_json': json.dumps(list(Course.objects.values()), sort_keys=True, default=str),
    }
    return render(request, 'pages/courses.html', context)


@login_required
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


@login_required
def reporting(request):
    employee = get_object_or_404(Employee, user=request.user)
    employeeTasks = Task.objects.filter(Employee=employee)
    completed_tasks = Task.objects.filter(Employee=employee, Status=1)
    task_progress = len(completed_tasks)/len(employeeTasks) * 100
    PerformanceAsc = Performance.objects.all().order_by("TotalPoints")
    PerformanceDes = Performance.objects.all().order_by("-TotalPoints")

    achieved_percentage = random.randint(0, 100)
    top_employees = [{'name': f'Employee {i}','points': random.randint(50, 100)} for i in range(1, 6)]
    public_courses = [{'name': f'Course {i}', 'revenue': random.randint(5000, 20000), 'trainer':f'Trainer {i}'} for i in range(1, 6)]
    departments_data = [{'department': f'Department {i}', 'progress': random.randint(0, 100), 'employees': random.randint(5, 20)} for i in range(1, 6)]
    low_performance_employees = [{'name': f'Employee {i}', 'points': random.randint(0, 49)} for i in range(1, 6)]

    sales_Data = Salesman.objects.get(Employee=employee)
    min_target_value = sales_Data.SalesTarget * (sales_Data.SalesAchievement)/100
    min_target = "%.1f" % round(min_target_value, 2)
    sales_progress = sales_Data.SalesTarget * (sales_Data.SalesProgress)/100

    context = {
        'employee': employee,
        'task_progress': task_progress,
        'min_target': min_target,
        'achieved_percentage': achieved_percentage,
        'top_employees': top_employees,
        'public_courses': public_courses,
        'departments_data': departments_data,
        'low_performance_employees': low_performance_employees,
        'sales_Data': sales_Data,
        'sales_progress': sales_progress,
        "PerformanceAsc": PerformanceAsc,
        "PerformanceDes": PerformanceDes,
        "PerformanceJson": json.dumps(list(Performance.objects.values()), sort_keys=True, default=str),
        'employee_json': json.dumps(list(Employee.objects.values()), sort_keys=True, default=str)
    }
    return render(request, 'pages/reporting.html', context)


@login_required
def employees_tracking(request):
    employee = get_object_or_404(Employee, user=request.user)
    if 'q' in request.GET:
        qe = request.GET['q']
        employee_list = Employee.objects.filter(
            Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    else:
        employee_list = Employee.objects.all()

    context = {
        'employee': employee,
        'employees': employee_list,
    }
    return render(request, 'pages/task_tracking.html', context)


@login_required
def employees_tracking_detail(request, id):
    employee = get_object_or_404(Employee, user=request.user)
    selected_employee = Employee.objects.get(pk=id)
    completed_tasks = Task.objects.filter(Employee=selected_employee, Status=1)
    overdue_tasks = Task.objects.filter(Employee=selected_employee, Status=3)
    inprogress_tasks = Task.objects.filter(
        Employee=selected_employee, Status=2)
    inprogress_tasks_all = Task.objects.filter(Status=2)
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
        'id': id,
        'completed_tasks': completed_tasks,
        'inprogress_tasks': inprogress_tasks,
        'overdue_tasks': overdue_tasks,
        'inprogress_tasks_all': inprogress_tasks_all,


    }
    return render(request, 'pages/task_tracking_detail.html', context)


@login_required
def my_tasks(request):
    employee = get_object_or_404(Employee, user=request.user)
    completed_tasks = Task.objects.filter(Employee=employee, Status=1)
    overdue_tasks = Task.objects.filter(Employee=employee, Status=3)
    inprogress_tasks = Task.objects.filter(
        Employee=employee, Status=2)
    if 'q' in request.GET:
        q = request.GET['q']
        tasks_list = Task.objects.filter(Q(TaskName__icontains=q), Employee=employee)
    else:
        tasks_list = Task.objects.filter(Employee=employee)

    context = {
        'employee': employee,
        'tasks': tasks_list,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'inprogress_tasks': inprogress_tasks,

    }
    return render(request, 'pages/my_tasks.html', context)


def my_tasks_detail(request, id):
    employee = get_object_or_404(Employee, user=request.user)
    selected_task = Task.objects.get(pk=id)

    # if 'qe' in request.GET:
    #     qe = request.GET['qe']
    #     employee_list = Employee.objects.filter(
    #         Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    # else:
    #     employee_list = Employee.objects.all()

    #     # print(selected_employee.Task_set.all())

    context = {
        'employee': employee,
        'selected_task': selected_task,
    }
    return render(request, 'pages/my_task_detail.html', context)


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, 'pages/logout.html')


#Unfinished for activity
@login_required
def my_activity(request):
    employee = get_object_or_404(Employee, user=request.user)
    activity_logs = Activity.objects.filter(Employee=employee)

    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     clients_list = Client.objects.filter(
    #         Q(FirstName__icontains=q) | Q(LastName__icontains=q))
    #     print(q)
    # else:
    #     clients_list = Client.objects.all()

    context = {
        # 'clients': clients_list,
        'employee': employee,
        'activities':activity_logs,
        # 'client_json': json.dumps(list(Client.objects.values())),
    }
    return render(request, 'pages/activity-log.html', context)



@login_required
def create_activity(request):
    employee = get_object_or_404(Employee, user=request.user)



    if request.method == 'POST':
        if len(request.POST['ActivityName'].strip()) > 0:
            activity_name = request.POST['ActivityName']
            activity_desc = request.POST['Description']
            activity_project = request.POST['Project']
            activity_time = request.POST['DoneDate']
            Activity.objects.create(ActivityName=activity_name,Description=activity_desc,Project=activity_project,DoneDate=activity_time,Employee=employee)
        return redirect('my-activity')
    context= {
    'employee':employee,
        }
    return render(request,'pages/add-activity.html',context)


@login_required
def update_activity(request,id):
    employee = get_object_or_404(Employee, user=request.user)
    selected_activity = Activity.objects.get(pk=id)

    if request.method == 'POST':
        if len(request.POST['ActivityName'].strip()) > 0:
            activity_name = request.POST['ActivityName']
            activity_desc = request.POST['Description']
            activity_project = request.POST['Project']
            activity_time = request.POST['DoneDate']
            Activity.objects.filter(pk=id).update(ActivityName=activity_name,Description=activity_desc,Project=activity_project,DoneDate=activity_time,Employee=employee)
        return redirect('my-activity')
    context ={
        "employee":employee,
        'selected_activity':selected_activity
    }
    return render(request,'pages/update-activity.html',context)



@login_required
def delete_activity(request,id):
    Activity.objects.filter(pk=id).delete()
    return redirect('my-activity')


@login_required
def activity_detail(request,id):
    employee = get_object_or_404(Employee, user=request.user)
    selected_activity = Activity.objects.get(pk=id)

    context ={
        "employee":employee,
        'selected_activity':selected_activity
    }
    return render(request,'pages/activity-detail.html',context)


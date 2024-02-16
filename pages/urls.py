from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('register_user_email', views.register_username_email,
         name='register-user-email'),
    path('register_password', views.register_password, name='register-password'),
    path('trainer', views.trainer, name='trainers'),
    path('course', views.course, name='courses'),
    path('client', views.client, name='clients'),
    path('reporting', views.reporting, name='reporting'),
    path('employee', views.employee, name='employees'),
    path('employees/tracking', views.employees_tracking, name='employees-tracking'),
    path('employees/tracking/<int:id>', views.employees_tracking_detail,
         name='employees-tracking-detail'),
    path('employee_profile/', views.employee_profile, name='employee_profile'),
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


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


    # //////Reset Views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_password.html'),
         name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_send.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),
]

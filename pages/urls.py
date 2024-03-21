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
    path('employee_profile/my-tasks', views.my_tasks, name='my-tasks'),
    path('employee_profile/my-tasks/<int:id>',
         views.my_tasks_detail, name='my-tasks-detail'),
     # activity
    path('employee_profile/my-activity', views.my_activity, name='my-activity'),
    path('employee_profile/my-activity/add-activity', views.create_activity, name='add-activity'),
    path('employee_profile/my-activity/add-activity/<int:id>', views.update_activity, name='update-activity'),

    path('employee_profile/my-activity/<int:id>', views.delete_activity, name='delete-activity'),

    path('employee_profile/my-activity/detail/<int:id>', views.activity_detail, name='my-activity-detail'),
     
     #chatbot
      path('employee_profile/ai-assistant', views.ai_assistant, name='ai-assistant'),

     #  path('getResponse',views.getResponse,name='getResponse'),

     # logout

    path('logout',
         views.logout_user, name='logout'),


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

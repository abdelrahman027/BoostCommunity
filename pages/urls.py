from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('trainer', views.trainer, name='trainers'),
    path('course', views.course, name='courses'),
    path('employee_profile/', views.employee_profile, name='employee_profile'),
]

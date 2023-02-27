from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='home'),
    path('student/', views.student_home, name='student_home'),
    path('teacher/', views.teacher_home, name='teacher_home'),
    path('',views.home,name='home')
]


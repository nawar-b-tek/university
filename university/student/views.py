from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from student.models import Student_Subject, Student, Teacher, Classes, Subject


def home(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect('student_resultat')
        elif request.user.is_teacher:
            return redirect('teacher_home')
    return render(request, 'home.html')


@login_required
@user_passes_test(lambda u: u.is_student)
def student_resultat(request):
    query_set1 = Student.objects.filter(student_profile=request.user).first()
    query_set2 = Student_Subject.objects.filter(student=query_set1)
    return render(request, 'student_homepage.html', {'notes': query_set2, 'user': query_set1})


@login_required
@user_passes_test(lambda u: u.is_teacher)
def teacher_home(request):
    return render(request,'teacher_homepage.html')

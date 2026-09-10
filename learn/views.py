from django.shortcuts import render, redirect
from learn.models import Course
from accounts.models import User
# Create your views here.

def course_add(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        course_desc = request.POST['course_desc']
        course_tutor_name = request.POST['course_tutor_name']
        course_price = request.POST['course_price']
        course_video = request.FILES['course_video']

        Course.objects.create(
            course_name = course_name,
            course_desc = course_desc,
            course_tutor_name = course_tutor_name,
            course_price = course_price,
            course_video = course_video
        )
        return redirect("course")
    return render(request, "courseadd.html")

def course(request):
    courses = Course.objects.all()
    
    return render(request, "course.html", context = {"courses":courses,
        "user":request.user,
    })
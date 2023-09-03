from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

from .models import UserExtention, User, Record, Merit


def index(request):
    merits = Merit.objects.all()
    return render(request, "main/index.html", {"merits": merits})


@login_required(login_url="/login/")
def profile(request):
    db_grade = get_object_or_404(UserExtention, user=request.user.id).grade
    #records = Record.objects.filter(student=request.user.id)
    records = Record.objects.filter(Q(student=request.user.id) | Q(teacher=request.user.id))

    total_points = 100
    for record in records:
        total_points += record.merit.points

    context = {
        "grade": db_grade,
        "total_points": total_points,
        "records": records,
        "classes": range(1, 13),
    }
    return render(request, "main/profile.html", context)


@permission_required("main.add_record", login_url="/profile/")
@login_required(login_url="/login/")
def grade_form(request, user_grade):
    students = UserExtention.objects.filter(grade=user_grade)
    merits = Merit.objects.all()
    context = {
        "students": students,
        "merits": merits,
    }
    return render(request, "main/grade_form.html", context)


@permission_required("main.add_record", login_url="/profile/")
@login_required(login_url="/login/")
def grade_form_post(request):
    db_student = User.objects.get(id=int(request.POST["student-names"]))
    db_merit = Merit.objects.get(id=int(request.POST["merit-names"]))
    record = Record(
        teacher=request.user,
        student=db_student,
        merit=db_merit,
        comment=request.POST["comment"],
    )
    record.save()
    return redirect("profile")


def top_students(request):
    users = UserExtention.objects.exclude(grade=0)
    top = []
    for user in users:
        records = Record.objects.filter(student=user.user)
        total_points = 100
        for record in records:
            total_points += record.merit.points
        user.total_points = total_points
        top.append(user)

    top.sort(key=lambda x: x.total_points, reverse=True)
    top = top[:10]
    print(top)

    return render(request, "main/top_students.html", {"students": top})

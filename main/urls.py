from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("grade/<int:user_grade>", views.grade_form, name="grade_form"),
    path("grade/post/", views.grade_form_post, name="grade_form_post"),
    path("top_students/", views.top_students, name="top_students"),
]
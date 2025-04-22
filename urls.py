from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("course/<int:pk>/", views.course, name="course"),
    path("profile/add", views.profile_add, name="profile_add"),
    path("course/add", views.course_add, name="course_add"),
    path("profiles/", views.profile_list, name="profile_list")
    ]



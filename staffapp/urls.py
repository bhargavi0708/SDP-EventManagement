from django.urls import path
from . import views

urlpatterns = [
    path("staff/auth/check", views.studentlogincheck, name="staff_login_check"),
    path("staff/dashboard", views.studenthome, name="staff_dashboard"),
    path("staff/logout", views.studentlogout, name="staff_logout"),
    path("staff/events", views.availablecourses, name="staff_events"),
    path("staff/events/<int:course_id>/join", views.enrollcourse, name="staff_join_event"),
    path("staff/schedule", views.studentcourses, name="staff_schedule"),
]

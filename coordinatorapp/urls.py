from django.urls import path
from . import views

urlpatterns = [
    path("coordinator/auth/check", views.instructorlogincheck, name="coordinator_login_check"),
    path("coordinator/dashboard", views.instructorhome, name="coordinator_dashboard"),
    path("coordinator/logout", views.instructorlogout, name="coordinator_logout"),
    path("coordinator/events", views.instructorcourses, name="coordinator_events"),
]

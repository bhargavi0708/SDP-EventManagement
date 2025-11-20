from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path("admin/login/check", views.adminlogincheck, name="admin_login_check"),
    path("admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
    path("admin/logout", views.logout, name="admin_logout"),

    # Staff CRUD
    path("admin/staff/add", views.admin_staff_add, name="admin_staff_add"),
    path("admin/staff", views.admin_staff_list, name="admin_staff_list"),
    path("admin/staff/<int:student_id>/edit", views.admin_staff_edit, name="admin_staff_edit"),
    path("admin/staff/<int:student_id>/delete", views.admin_staff_delete, name="admin_staff_delete"),

    # Coordinator CRUD
    path("admin/coordinators/add", views.admin_coordinator_add, name="admin_coordinator_add"),
    path("admin/coordinators", views.admin_coordinator_list, name="admin_coordinator_list"),
    path("admin/coordinators/<int:instructor_id>/edit", views.admin_coordinator_edit, name="admin_coordinator_edit"),
    path("admin/coordinators/<int:instructor_id>/delete", views.admin_coordinator_delete, name="admin_coordinator_delete"),

    # Event CRUD
    path("admin/events/add", views.admin_event_add, name="admin_event_add"),
    path("admin/events", views.admin_event_list, name="admin_event_list"),
    path("admin/events/<int:course_id>/edit", views.admin_event_edit, name="admin_event_edit"),
    path("admin/events/<int:course_id>/delete", views.admin_event_delete, name="admin_event_delete"),

    # Assignments
    path("admin/assignments", views.admin_assignments, name="admin_assignments"),
]

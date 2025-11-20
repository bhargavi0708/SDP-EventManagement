from django.contrib import admin
from .models import Course, Admin, Student, Instructor, Enrollment

admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Enrollment)

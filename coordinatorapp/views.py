from django.shortcuts import render, redirect
from django.contrib import messages
from adminapp.models import Instructor, Course, Enrollment

# Create your views here.

def instructorlogincheck(request):
    if request.method == 'POST':
        instructorid = request.POST.get('instructorid')
        password = request.POST.get('password')
        
        try:
            instructor = Instructor.objects.get(instructorid=instructorid, password=password)
            request.session['coordinator_id'] = instructor.id
            request.session['role'] = 'coordinator'
            request.session['coordinator_name'] = instructor.fullname
            messages.success(request, f'Welcome {instructor.fullname}!')
            return redirect('coordinator_dashboard')
        except Instructor.DoesNotExist:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    return redirect('login')

def instructorlogout(request):
    if 'role' in request.session:
        del request.session['role']
    if 'coordinator_id' in request.session:
        del request.session['coordinator_id']
    if 'coordinator_name' in request.session:
        del request.session['coordinator_name']
    messages.info(request, 'Logged out successfully!')
    return redirect('login')

def instructorhome(request):
    if 'role' not in request.session or request.session['role'] != 'coordinator':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    instructor = Instructor.objects.get(id=request.session['coordinator_id'])
    courses = Course.objects.filter(instructor_id=instructor.id)
    
    context = {
        'instructor': instructor,
        'courses_count': courses.count(),
    }
    return render(request, 'coordinator/coordinatorhome.html', context)

def instructorcourses(request):
    if 'role' not in request.session or request.session['role'] != 'coordinator':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    instructor = Instructor.objects.get(id=request.session['coordinator_id'])
    courses = Course.objects.filter(instructor_id=instructor.id)
    
    # Get enrollments for each course
    course_details = []
    for course in courses:
        enrollments = Enrollment.objects.filter(course=course)
        course_details.append({
            'course': course,
            'enrollment_count': enrollments.count(),
            'enrollments': enrollments,
        })
    
    context = {
        'course_details': course_details,
        'instructor': instructor,
    }
    return render(request, 'coordinator/coordinatorevents.html', context)

from django.shortcuts import render, redirect
from django.contrib import messages
from adminapp.models import Student, Course, Enrollment

def studentlogincheck(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        password = request.POST.get('password')
        
        try:
            student = Student.objects.get(studentid=studentid, password=password)
            request.session['staff_id'] = student.id
            request.session['role'] = 'staff'
            request.session['staff_name'] = student.fullname
            messages.success(request, f'Welcome {student.fullname}!')
            return redirect('staff_dashboard')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    return redirect('login')

def studentlogout(request):
    if 'role' in request.session:
        del request.session['role']
    if 'staff_id' in request.session:
        del request.session['staff_id']
    if 'staff_name' in request.session:
        del request.session['staff_name']
    messages.info(request, 'Logged out successfully!')
    return redirect('login')

def studenthome(request):
    if 'role' not in request.session or request.session['role'] != 'staff':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    student = Student.objects.get(id=request.session['staff_id'])
    enrolled_courses = Enrollment.objects.filter(student=student)
    
    context = {
        'student': student,
        'enrolled_count': enrolled_courses.count(),
    }
    return render(request, 'staff/staffhome.html', context)

def availablecourses(request):
    if 'role' not in request.session or request.session['role'] != 'staff':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    student = Student.objects.get(id=request.session['staff_id'])
    enrolled_course_ids = Enrollment.objects.filter(student=student).values_list('course_id', flat=True)
    available_courses = Course.objects.exclude(id__in=enrolled_course_ids)
    
    context = {
        'courses': available_courses,
        'student': student,
    }
    return render(request, 'staff/availableevents.html', context)

def enrollcourse(request, course_id):
    if 'role' not in request.session or request.session['role'] != 'staff':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    student = Student.objects.get(id=request.session['staff_id'])
    course = Course.objects.get(id=course_id)
    
    # Check if already enrolled
    if Enrollment.objects.filter(student=student, course=course).exists():
        messages.warning(request, 'You are already scheduled for this event!')
        return redirect('staff_schedule')
    
    Enrollment.objects.create(student=student, course=course)
    messages.success(request, f'Successfully scheduled for {course.coursetitle}!')
    return redirect('staff_schedule')

def studentcourses(request):
    if 'role' not in request.session or request.session['role'] != 'staff':
        messages.error(request, 'Please login first!')
        return redirect('login')
    
    student = Student.objects.get(id=request.session['staff_id'])
    enrollments = Enrollment.objects.filter(student=student)
    
    context = {
        'enrollments': enrollments,
        'student': student,
    }
    return render(request, 'staff/staffassignments.html', context)

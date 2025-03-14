from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses_page(request):
    return render(request, 'courses.html')

def add_student_form(request):
    return render(request, 'add_student.html')

def search_student_form(request):
    return render(request, 'search_student.html')

def get_courses(request):
    # Sample lists of courses
    pg_courses = ["M.Sc Computer Science", "MBA", "M.A. Economics"]
    ug_courses = ["B.Sc Computer Science", "BBA", "B.A. Economics"]
    
    data = {
        "pg_courses": pg_courses,
        "ug_courses": ug_courses
    }
    return JsonResponse(data)

def search_student(request):
    student_id = request.GET.get('student_id')
    if student_id is None:
        return JsonResponse({"error": "No student ID provided"}, status=400)
    
    try:
        student = Student.objects.get(student_id=student_id)
        data = {
            "student_id": student.student_id,
            "name": student.name,
            "email": student.email,
        }
        return JsonResponse(data)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

@csrf_exempt  # Only use this for testing and debugging; not recommended for production
def add_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        if not student_id or not name or not email:
            return JsonResponse({"error": "Missing data"}, status=400)
        
        Student.objects.create(student_id=student_id, name=name, email=email)
        return JsonResponse({"success": "Student added successfully"}, status=201)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)


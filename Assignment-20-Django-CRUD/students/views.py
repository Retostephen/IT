from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import StudentForm
from .models import Student


class CustomLoginView(LoginView):
    template_name = "students/login.html"


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "students/signup.html", {"form": form})


@login_required
def dashboard(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all()
    if query:
        students = students.filter(full_name__icontains=query)

    context = {
        "students": students,
        "total_students": Student.objects.count(),
        "query": query,
    }
    return render(request, "students/dashboard.html", context)


@login_required
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("dashboard")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("dashboard")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/student_form.html", {"form": form, "title": "Edit Student"})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("dashboard")
    return render(request, "students/student_confirm_delete.html", {"student": student})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})

from django.shortcuts import redirect, render, get_object_or_404
from .form import StudentForm
from .models import Student

# Create your views here.


def create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update_view(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/students")

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect("/students")

    context = {
        'student': student
    }
    return render(request, 'delete.html', context)


def detail_view(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    context = {
        'student': student
    }
    return render(request, 'detail.html', context)


def list_view(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'list.html', context)

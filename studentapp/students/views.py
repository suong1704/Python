from black import format_file_contents
from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from .forms import StudentForm,RawStudentForm
from .models import Student


# Create your views here.

# def create_view(request):
#     form = RawStudentForm()
#     if request.method == 'POST':
#         form = RawStudentForm(request.POST or None)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Student.objects.create(**form.cleaned_data)
#             form = RawStudentForm()
#         else:
#             print(form.errors)

#     context = {
#         'form': form
#     }
#     return render(request, 'students/create.html', context)

# def create_view(request):
#     if request.method=="POST":
#         new_code = request.POST.get("code")
#         print(new_code)
#         # Student.objects.create(code=new_code)

#     context = {}
#     return render(request, 'create.html', context)

def create_view(request):
    initial_value = {
        'code' : '102145864',
        'name' : 'Sương',
    }
    form = StudentForm(request.POST or None , initial=initial_value)
    if form.is_valid():
        form.save()
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'students/create.html', context)
def student_create_view(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudentForm()
    context = {
        'form': form ,
    }
    return render(request , 'students/create.html' , context)
def student_detail_view(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id = id)
    context = {
        'student' : student
    }
    # return render(request, 'students/detail.html' , {"student":student})
    return render(request, 'students/detail.html' , context)
def student_update_view(request, id):
    student = get_object_or_404(Student , id=id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == "POST":
        form.save()
        return redirect('/students')
    context = {
        'form': form,
    }
    return render(request, 'students/update.html', context)
def student_delete_view(request , id):
    student = get_object_or_404(Student , id = id)
    if request.method == "POST":
        student.delete()
        return redirect('/students')
    context = {
        'student': student,
    }
    return render(request , 'students/delete.html' , context)
def student_list_view(request):
    keyword = request.GET.get('keyword')
    if keyword:
        queryset = Student.objects.filter(code__icontains=keyword)
    else: 
        queryset = Student.objects.all()
    context = {
        'keyword': keyword,
        'students' : queryset.order_by('code'),
    }
    return render(request , 'students/list.html' , context)

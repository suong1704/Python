from black import format_file_contents
from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from .forms import VehicleForm
from .models import Vehicles

def create_view(request):
    initial_value = {
        'code' : '34K-123458',
        'name' : 'Sirius',
        'model' : 'Yamaha'
    }
    form = VehicleForm(request.POST or None , initial=initial_value)
    if form.is_valid():
        form.save()
        form = VehicleForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)
def student_create_view(request):
    # obj = Student.objects.get(id=10)
    # form = StudentForm(request.POST or None, instance=obj)
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VehicleForm()
    context = {
        'form': form ,
    }
    return render(request , 'create.html' , context)
def detail_view(request,id):
    # vehicle = {
    #     'code' : '34K-123458',
    #     'name' : 'Sirius',
    #     'model' : 'Yamaha'
    # }
    # student = Student.objects.get(id=id)
    vehicle = get_object_or_404(Vehicles, id = id)
    context = {
        'vehicle' : vehicle
    }
    # return render(request, 'students/detail.html' , {"student":student})
    return render(request, 'detail.html' , context)
def update_view(request, id):
    vehicle = get_object_or_404(Vehicles , id=id)
    # vehicle = {
    #     'code' : '34K-123458',
    #     'name' : 'Sirius',
    #     'model' : 'Yamaha'
    # }
    form = VehicleForm(request.POST or None, instance=vehicle)
    if request.method == "POST":
        form.save()
        return redirect('/QL')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)
def delete_view(request,id ):
    vehicle = get_object_or_404(Vehicles , id = id)
    # vehicle = {
    #     'code' : '34K-123458',
    #     'name' : 'Sirius',
    #     'model' : 'Yamaha'
    # }
    if request.method == "POST":
        vehicle.delete()
        return redirect('/QL')
    context = {
        'vehicle': vehicle,
    }
    
    return render(request , 'delete.html' , context)
def list_view(request):
    keyword = request.GET.get('keyword')
    if keyword:
        queryset = Vehicles.objects.filter(code__icontains=keyword)
    else: 
        queryset = Vehicles.objects.all()
    context = {
        'keyword': keyword,
        'vehicles' : queryset.order_by('code'),
    }
    return render(request , 'list.html' , context)

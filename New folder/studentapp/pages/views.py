from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    context = {
        'name': 'Vu',
        'skills': ['c#','html','django']
    }
    return render(request, 'home.html',context)
def contact_view(request):
    return render(request, 'contact.html',{})
def about_view(request):
    return render(request, 'about.html',{})
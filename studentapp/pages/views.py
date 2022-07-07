from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student

# Create your views here.
def home_view(request):
    # context = {
    #     'name': 'Suong',
    #     'skills': ['c#', 'html', 'django'],
    #     'content' : '<div class="alert alert-primary" role="alert">Hello Django!</div>'
    # }
    # return render(request, 'pages/home.html', context)
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
    
def contact_view(request):
    return render(request, 'pages/contact.html', {})

def about_view(request):
    return render(request, 'pages/about.html', {})

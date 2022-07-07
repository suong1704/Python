from django.shortcuts import render


from QL.models import Vehicles

# Create your views here.
def home_view(request):
    # keyword = request.GET.get('keyword')
    # if keyword:
    #     queryset = Vehicles.objects.filter(code__icontains=keyword)
    # else: 
    #     queryset = Vehicles.objects.all()
    # context = {
    #     'keyword': keyword,
    #     'Vehicles' : queryset.order_by('code'),
    # }
    # return render(request , 'QL/list.html' , context)
    return render(request, 'home.html', {})
    
def contact_view(request):
    return render(request, 'contact.html', {})

def about_view(request):
    return render(request, 'about.html', {})
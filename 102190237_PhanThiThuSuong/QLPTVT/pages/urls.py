from django.urls import  path
from .views import about_view, contact_view, home_view


urlpatterns = [
    path('', home_view , name='home'),
    path('contact', contact_view , name='contact'),
    path('about', about_view , name='about'),
    
]
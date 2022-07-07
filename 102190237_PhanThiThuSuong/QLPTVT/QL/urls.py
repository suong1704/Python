from django.urls import  path
from .views import create_view, detail_view, list_view, delete_view, update_view


urlpatterns = [
    path('', list_view , name='list'),
    path('create', create_view , name='create'),
    path('detail/<int:id>', detail_view , name='detail'),
    path('detele/<int:id>', delete_view , name='delete'),
    path('update/<int:id>', update_view , name='update'),
    
]
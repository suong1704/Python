from django.urls import  path

from pages.views import home_view
from .views import student_list_view, student_delete_view, student_create_view , student_detail_view, student_update_view


urlpatterns = [
    # path('detail/<int:id>', detail_view , name='detail'),
    # path('create', create_view , name='create'),
   
    path('', student_list_view , name='list'),
    path('detail/<int:id>', student_detail_view , name='detail'),
    path('create', student_create_view , name='create'),
    path('update/<int:id>' , student_update_view , name='update'),
    path('delete/<int:id>' , student_delete_view , name='delete'),
    
]
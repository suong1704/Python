import imp
from django.contrib import admin

# Register your models here.
from .models import Student, Department, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'email', 'department')
    list_filter = ('department',)

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
from sqlite3 import Date
from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name}({self.id})"
       
    
class Student(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(default=25)
    gender = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    department = models.ForeignKey(Department,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,  
    )
    def __str__(self):
        return f"{self.code} - {self.name}({self.id})"
    def get_absolute_url(self):
        return reverse("detail" , kwargs={'id':self.id})
        # return f"/students/{self.id}"     
class Course(models.Model):
    name = models.TextField(max_length=256)
    limit = models.IntegerField(default=30)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    Student = models.ManyToManyField(Student, blank=True, null=True)

    def __str__(self):
        return f"{self.name}({self.id})"
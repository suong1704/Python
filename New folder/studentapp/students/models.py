from django.db import models
from django.urls import reverse
# Create your models here.
class Department (models.Model):
    name = models.TextField(max_length=256)

class Student(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255)
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(default=25)
    gender = models.BooleanField(default=True)
    email = models.TextField(blank=False, null=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=False,
        null=True
    )
    def get_absolute_url(self):
        return reverse("update", kwargs={"id":self.id})
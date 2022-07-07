from django.db import models
from django.urls import reverse
# Create your models here.


class Vehicles(models.Model):
    # Biển số
    code = models.TextField(max_length=256, blank=True , null=True)
    # Tên
    name = models.TextField(max_length=256, blank=True , null=True)
    # Hãng sản xuất
    model = models.TextField(max_length=256, blank=True , null=True)

    def __str__(self):
        return f"{self.name}({self.id})"
    def get_absolute_url(self):
        return reverse("detail" , kwargs={'id':self.id})
class Vehicle(models.Model):
    # Biển số
    code = models.TextField(max_length=256, blank=True , null=True)
    # Tên
    name = models.TextField(max_length=256, blank=True , null=True)
    # Hãng sản xuất
    model = models.TextField(max_length=256, blank=True , null=True)

    def __str__(self):
        return f"{self.name}({self.id})"
    def get_absolute_url(self):
        return reverse("detail" , kwargs={'id':self.id})
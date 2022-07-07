import email
from pyexpat import model
from attr import field
from django import forms
from .models import  Vehicles

class VehicleForm(forms.ModelForm):
    code    =   forms.CharField(
                label='MSSV',
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : '81A-12456',
                })

    )
    name    =   forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Yamaha',
                })
    )
    model =   forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Yamaha',
                })
    )
    
   
    class Meta:
        model= Vehicles
        fields= [
            'code',
            'name',
            'model',
        ]



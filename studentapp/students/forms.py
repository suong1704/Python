import email
from pyexpat import model
from attr import field
from django import forms
from .models import Student, Department

class StudentForm(forms.ModelForm):
    code    =   forms.CharField(
                label='MSSV',
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : '102190237',
                })

    )
    name    =   forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Họ và Tên',
                })
    )
    age =   forms.IntegerField(
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : '20',
                })
    )
    gender =   forms.BooleanField(
               required=False
    )
    
    address =   forms.CharField(
                # initial="Việt Nam",
                widget=forms.Textarea(attrs={
                    'class' : 'form-control',
                    'row' : 10,
                    'placeholder' : 'Gia Lai',
                })
    )
    email =   forms.EmailField(
                widget=forms.EmailInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'a@gmail.com',
                })
    )
   
    class Meta:
        model= Student
        fields= [
            'code',
            'name',
            'age',
            'gender',
            'address',
            'email',
            'department',
        ]
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     objs = Department.objects.all()
    #     departments = [(i.id, i.name) for i in objs]
    #     self.fields['department'].choices = departments

    def clean_code(self , *args, **kwargs):
        code = self.cleaned_data['code']
        if  not code.isnumeric():
            raise forms.ValidationError("The code should be numeric only!")
        if  (not len(code) == 9):
            raise forms.ValidationError("The code must include 9 digits!")
        return code
    def clean_email(self , *args, **kwargs):
        email = self.cleaned_data['email']
        if  not email.endswith("@gmail.com"):
            raise forms.ValidationError("Invalid email")
        return email
    def department(self , *args, **kwargs):
        department = self.cleaned_data['department']
        return department.name
    def clean_gender(self , *args, **kwargs):
        gender = self.cleaned_data['gender']
        if  gender == False:
            return gender
        return gender
    
    
class RawStudentForm(forms.Form):
    code    =   forms.CharField(
                label='MSSV',
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : '102190237',
                })

    )
    name    =   forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Họ và Tên',
                })
    )
    address =   forms.CharField(
                # initial="Việt Nam",
                widget=forms.Textarea(attrs={
                    'class' : 'form-control',
                    'row' : 10,
                    'placeholder' : 'Gia Lai',
                })
    )
    # email =   forms.EmailField(
    #             widget=forms.EmailInput(attrs={
    #                 'class' : 'form-control',
    #                 'placeholder' : 'a@gmail.com',
    #             })
    # )
    def clean_code(self , *args, **kwargs):
        code = self.cleaned_data['code']
        if  not code.isnumeric():
            raise forms.ValidationError("The code should be numeric only!")
        return code
    # def clean_email(self , *args, **kwargs):
    #     email = self.cleaned_data['email']
    #     if  not email.endswith("@gmail.com"):
    #         raise forms.ValidationError("Invalid email")
    #     return email
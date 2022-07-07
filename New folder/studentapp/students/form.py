import code
from dataclasses import field
import email
from unicodedata import name
from django import forms
from .models import Department, Student
class StudentForm(forms.ModelForm):
    code = forms.CharField(
        label='MSSV',
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'MSSV'}
        )
    )
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
             attrs={'class':'form-control','placeholder':'Ho va ten'}
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'class':'form-control',
                'rows':'5',
                'cols':'10'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'class':'form-control',
            }
        )
    )
    class Meta:
        model = Student
        fields = ['code','name','address','email','department']
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        departmentObj = Department.objects.all()
        departments = [(i.id, i.name) for i in departmentObj]
        self.fields['department'].choices = departments

    def clean_code(self, *args, **kwargs):
        code = self.cleaned_data.get('code')
        if not code.isnumeric():
            raise forms.ValidationError("The Code should be numeric only!")
        return code
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("dut.udn.vn"):
            raise forms.ValidationError("The Email should end with dut.udn.vn")
        return email
    

# class RawStudentForm(forms.Form):
#     code = forms.CharField(
#         label='MSSV',
#         widget=forms.TextInput(
#             attrs={'class':'form-control','placeholder':'MSSV'}
#         )
#     )
#     name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#              attrs={'class':'form-control','placeholder':'Ho va ten'}
#         )
#     )
#     address = forms.CharField(
#         initial='Viet Nam',
#         widget=forms.Textarea(
#             attrs= {
#                 'class':'form-control',
#                 'rows':'5',
#                 'cols':'10'
#             }
#         )
#     )
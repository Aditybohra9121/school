from django.forms import ModelForm
from .models import Student
class addStudentForm(ModelForm):
    
    class Meta:
        model=Student
        fields=['name','age','gender']
        

from django import forms
from django.contrib.auth.models import User
from basic_app.models import Student,Placed_student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')



class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields="__all__"



class UpdateForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=('FirstName','LastName','Fagg_percentage','Sagg_percentage','Tagg_percentage','F_YroPassing','S_YroPassing','T_YroPassing','Total')



class PlacedstudentForm(forms.ModelForm):
	class Meta:
		model=Placed_student
		fields = ('FirstName', 'LastName','EmailID','Total','Company_name')

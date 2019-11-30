from django.db import models
#from phone_field import PhoneField

# Create your models here.
class Student(models.Model):
	Username=models.CharField(max_length=100)
	FirstName=models.CharField(max_length=100)
	LastName=models.CharField(max_length=100)
	EmailID=models.EmailField()
	MobileNumber=models.CharField(max_length=100)
	#For radio input
	GENDER_CHOICE=(
		('Male',"Male"),
		('Female',"Female"),
		)
	Gender = models.CharField(choices=GENDER_CHOICE , max_length=128)
	#BirthDay=models.DateField()
	Address=models.TextField()
	City=models.CharField(max_length=70)
	State=models.CharField(max_length=100)
	Country=models.CharField(max_length=100)
	ClassX_Board=models.CharField(max_length=100)
	ClassX_Percentage=models.FloatField(max_length=100)
	ClassX_YrOfPassing=models.CharField(max_length=100)
	ClassXII_Board=models.CharField(max_length=100)
	ClassXII_Percentage =models.FloatField(max_length=100)
	ClassXII_YrOfPassing=  models.CharField(max_length=100)
	Fagg_percentage=models.FloatField(max_length=100)
	F_YroPassing=models.CharField(max_length=100)
	Sagg_percentage=models.FloatField(max_length=100)
	S_YroPassing=models.CharField(max_length=100)
	Tagg_percentage=models.FloatField(max_length=100)
	T_YroPassing=models.CharField(max_length=100)
	Total=models.FloatField(max_length=100)
	class Meta:
		db_table="student"

class Placed_student(models.Model):
	Username = models.CharField(max_length=100)
	FirstName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	EmailID = models.EmailField()
	MobileNumber = models.CharField(max_length=100)
	Fagg_percentage = models.FloatField(max_length=100)
	F_YroPassing = models.CharField(max_length=100)
	Sagg_percentage = models.FloatField(max_length=100)
	S_YroPassing = models.CharField(max_length=100)
	Tagg_percentage = models.FloatField(max_length=100)
	T_YroPassing = models.CharField(max_length=100)
	Total = models.FloatField(max_length=100)
	Company_name=models.CharField(max_length=100)
	class Meta:
		db_table = "place_student"
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Student(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	father_name=models.CharField(max_length=100)
	mother_name=models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	# course_id=
	# department_id=


	def __str__(self):
		return self.name

class Staff(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address=models.CharField(max_length=500)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	# subject_id=
	# department_id=


	def __str__(self):
		return self.name


class Hod(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address=models.CharField(max_length=500)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	# department_id=


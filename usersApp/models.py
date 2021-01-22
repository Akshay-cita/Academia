from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from academics.models import Department,Course,Subject

# Create your models here.
class Student(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	father_name=models.CharField(max_length=100)
	mother_name=models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	course_id=models.ForeignKey(Course,on_delete=models.CASCADE())
	created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
	# dept_id=models.ForeignKey(Department,on_delete=models.CASCADE())


	def __str__(self):
		return self.name

class Staff(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address=models.CharField(max_length=500)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	dept_id=models.ForeignKey(Department,on_delete=models.CASCADE())
	subj_id=models.ForeignKey(Subject,on_delete=models.CASCADE())
	created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name


class Hod(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=500)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	address=models.CharField(max_length=500)
	contact_email=models.EmailField(max_length=100)
	contact_phone=PhoneNumberField(blank=True)
	# dept_id=models.ForeignKey(Department,on_delete=models.CASCADE())
	# course_id=models.ForeignKey(Course,on_delete=models.CASCADE())
	created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
	# department_id=


	def __str__(self):
		return self.name


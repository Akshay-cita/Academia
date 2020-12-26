from django.db import models
# from usersApp.models import Hod,Staff

# Create your models here.
class Department(models.Model):
	dept_name=models.CharField(max_length=50)
	hod_id=models.ForeignKey(Hod,on_delete=models.CASCADE())
	


	def __str__(self):
		return self.dept_name

class Course(models.Model):
	course_name=models.CharField(max_length=100)
	dept_id=models.ForeignKey(Department,on_delete=models.CASCADE())

	def __str__(self):
		return self.course_name

class Subject(models.Model):
	subject_name=models.CharField(max_length=100)
	subject_code=models.CharField(max_length=100)
	course_id=models.ForeignKey(Course,on_delete=models.CASCADE())
	dept_id=models.ForeignKey(Department,on_delete=models.CASCADE())
	



	def __str__(self):
		return self.subject_name


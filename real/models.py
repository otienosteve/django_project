from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=12)
    date_joined=models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    dept_head=models.CharField(max_length=55)

class Teacher(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'teachers/',default='')
    # dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)





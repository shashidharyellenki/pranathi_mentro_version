import datetime
from math import fabs
from django.db import models

# Create your models here.

# course modal
class Courses(models.Model):
    Course_name = models.CharField(max_length=100, blank=False)
    Start_date = models.DateField()
    End_date = models.DateField()
    Course_createdAt= models.DateField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.Course_name



# EVALUATION FORM
class Evaluation(models.Model):
    email = models.EmailField(max_length=100, blank=False)
    remarks = models.TextField(max_length=100, blank=False)
    marks = models.IntegerField(default=0)
    course_Id = models.IntegerField()


    def __str__(self):
        return str(self.email)
        
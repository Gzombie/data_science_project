# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#first model is the info of students
class student(models.Model):
	student_id=models.CharField(max_length=5,primary_key=True)
	name=models.CharField(max_length=30)
	standard=models.CharField(max_length=2)
	
#second model is the dct info
class classTestInfo(models.Model):
	dct_id=models.CharField(max_length=10,primary_key=True)
	subject=models.CharField(max_length=30)
	standard=models.CharField(max_length=2)
	main_module=models.CharField(max_length=50)
	sub_module=models.CharField(max_length=50)
	subjective=models.IntegerField()
	obejective=models.IntegerField()
	testDate=models.DateField()

class studentMarks(models.Model):
	Student_id=models.ForeignKey(student,on_delete=models.CASCADE)
	DCT_id=models.ForeignKey(classTestInfo,on_delete=models.CASCADE)
	correctSubjective=models.IntegerField()
	wrongSubjective=models.IntegerField()
	correctObjective=models.IntegerField()
	wrongObjective=models.IntegerField()
	total=models.DecimalField(max_digits=5,decimal_places=2)

	
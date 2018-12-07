# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#first model is the info of students
class student(models.Model):
	student_id=models.CharField(max_length=50,primary_key=True)
	name=models.CharField(max_length=30)
	standard=models.CharField(max_length=2)
	
#second model is the dct info
class classTestInfo(models.Model):
	dct_id=models.IntegerField(primary_key=True)
	subject=models.CharField(max_length=30)
	standard=models.CharField(max_length=5)
	main_module=models.CharField(max_length=50)
	sub_module=models.CharField(max_length=50)
	subjective_total=models.IntegerField()
	objective_total=models.IntegerField()
	testDate=models.CharField(max_length=10)

class studentMarks(models.Model):
	Student_id=models.CharField(max_length=50)
	DCT_id=models.IntegerField()
	correctSubjective=models.IntegerField()
	wrongSubjective=models.IntegerField()
	correctObjective=models.IntegerField()
	wrongObjective=models.IntegerField()
	sub_total=models.DecimalField(max_digits=6,decimal_places=2)
	obj_total=models.DecimalField(max_digits=6,decimal_places=2)
	
	
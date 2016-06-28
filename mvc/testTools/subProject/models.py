from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.

class User(models.Model):
	id=models.IntegerField
	name=models.CharField(max_length=30)
	passwd=models.CharField(max_length=256)
	created_time=models.DateTimeField

	def __unicode__(self):
		return self.name

class UploadFileForm(forms.Form):
	title=forms.CharField(max_length=50,required=False)
	file=forms.FileField()
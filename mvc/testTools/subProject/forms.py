__author__ = 'junqingfjq'

from django import  forms

class AddForm(forms.Form):
	a=forms.IntegerField()
	b=forms.IntegerField()
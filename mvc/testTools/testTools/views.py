__author__ = 'junqingfjq'

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render_to_response


def index(request):
	return render_to_response("index.html")


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self,data,**kwargs):
		content=JSONRenderer().render(data)
		kwargs['content_type']='pplication/json'
		super(JSONResponse,self).__init__(content,**kwargs)


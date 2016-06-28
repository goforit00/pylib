#coding:utf-8
from django.http import HttpResponse

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.shortcuts import render_to_response

from abossTools.views import JSONResponse
from models import *
from core import core_service


import logging
logger = logging.getLogger(__name__)

#
# def index(requset):
# 	return HttpResponse(u"hello kitty")
#
#
# def add(request):
# 	if 'a' not in request.GET:
# 		a=10
# 	else:
# 		a=request.GET['a']
# 	if 'b' not in request.GET:
# 		b=20
# 	else:
# 		b=request.GET['b']
# 	c=int(a)+int(b)
# 	return HttpResponse(str(c))
#
# def add2(request,a,b):
# 	c=int(a)+int(b)
# 	return HttpResponse(str(c))
#
#
# def home(request):
# 	string ="这个是一个变量字符串"
# 	classList=["HTML","JAVA","CSS"]
# 	return render(request, 'subProject/home.html',{'string':string,'classList':classList})
#
# def form_add(request):
# 	if request.method=="POST":
# 		form = AddForm(request.POST)
# 		if form.is_valid():
# 			a=form.cleaned_data['a']
# 			b=form.cleaned_data['b']
# 			return HttpResponse(str(int(a)+int(b)))
# 	else:
# 		form=AddForm()
# 	return render(request,'subProject/index.html',{'form':form})

def _handle_file(file):
	pass

# @csrf_protect
def upload_file(request):
	if request.method=='POST':
		form =UploadFileForm(request.POST,request.FILES)
		print("get form")
		print(form.errors)
		if form.is_valid():
			_handle_file(request.FILES['file'])
			# return HttpResponseRedirect('subProject/success.html')
			print("in if")
			return render_to_response('subProject/index.html',context_instance=RequestContext(request))
	print("not in if")
	return render_to_response('subProject/success.html',context_instance=RequestContext(request))


def index(request):
	return render_to_response('subProject/index.html',context_instance=RequestContext(request))



def upload_oss_file(request):
	oss_env=request.GET['env']
	type=request.GET['type']
	logger.info("GET[env]:%s ,GET[env]:%s"%(oss_env,type))
	core_service.upload_oss(oss_env,type);

	return HttpResponse("")

def download_local(request):
	type=request.GET['type']
	logger.info("GET[type]:%s"%type)
	core_service.download_local(type)
	return HttpResponse("")


class DemoObject(models.Model):
	id="1"
	title="test title"
	code="test code"

	def __init__(self,id,title,code):
		self.id=id
		self.title=title
		self.code=code

	class Meta:
		ordering =('created',)

class DemoObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model=DemoObject
		fields=('id','title','code')


@csrf_exempt
def demo_list(request):
	if request.method=='GET':

		dos=[]
		dos.append(DemoObject(1,"aa","aa"))
		dos.append(DemoObject(2,"bb","bb"))
		print(dos)
		serializer=DemoObjectSerializer(dos,many=True)
		return JSONResponse(serializer.data)

	elif request.method=='POST':
		pass







"""abossTools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from ossTools import views as ossTools_views

urlpatterns = [
	url(r'^index',ossTools_views.index,name='index'),
	url(r'^upload/',ossTools_views.upload_file,name='uploadfile'),
	url(r'^demo/',ossTools_views.demo_list,name="demo"),
	url(r'^uploadOss/',ossTools_views.upload_oss_file,name="syncOss"),
	url(r'^downloadlocal/',ossTools_views.download_local,name="downloadlocal")


]

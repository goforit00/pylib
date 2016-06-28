__author__ = 'junqingfjq'

import hashlib
import urllib
import os
import sys
import shutil

import function_util
from ..base import base_executor

TMP_TARGET_FILE_DIR ="/tmp/download_path/"

def build_tmp_file_path(target_file):
	#build tmp path
	if not os.path.exists(TMP_TARGET_FILE_DIR):
		os.makedirs(TMP_TARGET_FILE_DIR)
		os.system("chmod 777 "+TMP_TARGET_FILE_DIR)

	#build target path
	target_file = target_file.strip()
	target_dir = target_file[0:target_file.rindex("/")]
	filename = target_file[target_file.rindex("/")+1:]
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)

	return  TMP_TARGET_FILE_DIR + filename


def download_file(url,tmpfile):

	download_command="wget '%s' -O %s " %(url,tmpfile)
	ret,stdout,stderr=function_util.popen(download_command)

	if(ret != 0):
		print("download file error")


def check_md5(file,md5_value):
	global BLOCK_SIZE

	md5_file = open(file, 'r')

	md5 = hashlib.md5()
	try:
		while True:
			data = md5_file.read(BLOCK_SIZE)
			if not data:
				break
			md5.update(data)
	except Exception,e:
		print(e)
	md5_file.close()
	hash = str(md5.hexdigest()).lower()

	if hash != md5_value and md5_value != "default_md5" :
		print("md5 error")

def move_file(srcfile,dstfile):
	shutil.move(srcfile,dstfile)


def download_by_url(url,md5_value,target_file):

	#build_path
	tmp_file=build_tmp_file_path(target_file)
	#download
	download_file(url,tmp_file)
	#check_md5
	check_md5(tmp_file,md5_value)
	#move file
	move_file(tmp_file,target_file)
	return True

def main():

	ct=base_executor.Context()
	ct.params_dict=function_util.build_dict(sys.argv[1:])
	url=ct.params_dict["url"]
	md5_value=ct.params_dict["md5_value"]
	target_file=ct.params_dict["target_file"]
	md5_value=str(md5_value).lower()

	if(False == download_by_url(url,md5_value,target_file)):
		sys.exit(0)
	else:
		sys.exit(1)

if __name__=='__main__':
	main()
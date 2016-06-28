__author__ = 'junqingfjq'

import os
import re
import hashlib
import zipfile
import tarfile
import subprocess


BLOCK_SIZE = 1024

def reverse_str_or_list(s):
	return s[::-1]


def travelTree(currentPath, count):
    if not os.path.exists(currentPath):
        return
    if os.path.isfile(currentPath):
        fileName = os.path.basename(currentPath)
        print('\t' * count + '├── ' + fileName)
    elif os.path.isdir(currentPath):
        print('\t' * count + '├── ' + currentPath)
        pathList = os.listdir(currentPath)
        for eachPath in pathList:
            travelTree(currentPath + '/' + eachPath, count + 1)


def get_dict_from_file(filename):
	dict_value=dict()
	with open(filename,"r") as f:
		for line in f.readlines():
			if line.strip():
				pos=str(line).find("=")
				if pos==-1:
					print("ParamsWarn:except key=value,actrually %s"%line )
					continue
				key=line[:pos].strip()
				value=line[pos+1:].strip()
				dict_value[key]=value
	return dict_value

def get_value_from_file(key,file_name):

	value = ""
	with open(file_name) as f:
		for line in f:
			position = line.find("=")
			if position==-1:
				continue
			k = line[:position]
			v = line[position+1:]
			k = k.strip()
			v = v.strip()
			if(k == key):
				value = v
				break
			else:
				continue
	return value

def replace_value_from_file(src_key,des_value,file_name):
	context=""
	flag=False
	with open(file_name,"r") as f:
		for line in f:
			position=line.find("=")
			if position==-1:
				context=context+line
				continue
			k=str(line[:position]).strip()
			if k==src_key:
				context=context+"%s = %s\n"%(src_key,des_value)
				flag=True
			else:
				context=context+line
	if not flag:
		context=context+"%s = %s\n"%(src_key,des_value)
	with open(file_name,"w") as f:
		f.write(context)


def save_var_to_file(filename,argv_str):

	argvs = argv_str.split(" ")
	len_of_argv = len(argvs)

	kv_str=""
	for i in range(0, len_of_argv - 1):
		if(argvs[i] == "-M"):
			argvs[i + 1] = argvs[i + 1].lstrip("'")
			argvs[i + 1] = argvs[i + 1].rstrip("'")
			kv_str = kv_str + " " + argvs[i + 1]

	f = open(filename, "w+")

	kv_argv=kv_str.split(" ")
	kv_num = len(kv_argv)

	for i in range(0, kv_num):
		if(kv_argv[i] != ""):
			data = kv_argv[i].split("=")
			if(len(data) > 1):
				data[0] = data[0].strip()
				data[1] = data[1].strip()
				key = data[0]
				value = data[1]
				os.system("sed -i '/^" + key + "[[:blank:]]*=/d' " + filename)   #delete lines
				f = open(filename, "a")
				f.write(key + " = " + value + "\n")       #add new line
				f.close()

def kvstr_convert_dict(kvstr,sep=" "):

	result_dict=dict()
	if kvstr == "":
		return result_dict
	kv_list=str(kvstr).split(sep)
	list_len=len(kv_list)
	for i in range(0,list_len):
		pos=kv_list[i].find("=")
		if(pos==-1):
			continue
		key=kv_list[i][0:pos]
		value=kv_list[i][pos+1:]
		key=key.strip()
		value=value.strip()
		result_dict[key]=value

	return result_dict


def getObjectByName(module_name,class_name):
	module=__import__(module_name)
	className=getattr(module,class_name)
	return className()


def copy_files(source_dir,  target_dir):

	if source_dir.find(".svn") > 0:
		return

	for file in os.listdir(source_dir):
		sourceFile = os.path.join(source_dir,  file)
		targetFile = os.path.join(target_dir,  file)
		if os.path.isfile(sourceFile):
			if not os.path.exists(target_dir):
				os.makedirs(target_dir)
			if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
				open(targetFile, "wb").write(open(sourceFile, "rb").read())
		if os.path.isdir(sourceFile):
			copy_files(sourceFile, targetFile)

def copy_file(source_file,target_file):

	if not os.path.exists(source_file):
		print("source file: %s not exist" % source_file )
		return False
	target_dir = ""
	if( target_file.find("/") != -1):
		position=target_file.rindex("/")
		target_dir = target_file[:position]
		if not os.path.exists(target_dir):
			os.makedirs(target_dir)
	open(target_file, "wb").write(open(source_file, "rb").read())



def zip_files(source_file_path,target_file_name):

	dir = source_file_path
	f=zipfile.ZipFile(target_file_name,'w',zipfile.ZIP_DEFLATED)

	for dirpath , dirnames , filenames in os.walk(dir):
		#print("dirpath:%s , dirnames%s ,filenames %s" %(dirpath,dirnames,filenames))
		for filename in filenames:
			zip_dir = "./"+dirpath[len(source_file_path):]
		#	print("filename:"+filename)
			if(filename != target_file_name):
		#		print("path:"+os.path.join(zip_dir,filename))
				f.write(os.path.join(dirpath,filename),os.path.join(zip_dir,filename))

	f.close()

def remove_files(target_dir):

	if not os.path.exists(target_dir):
		return
	for file in os.listdir(target_dir):
		target_file=os.path.join(target_dir,file)
		if( os.path.isfile(target_file)):
			os.remove(target_file)
		elif( os.path.isdir(target_file) ):
			remove_files(target_file+"/")
			os.rmdir(target_file)

#tar -xvf
def tarx_file(filename,tarx_path):

	if not os.path.exists(tarx_path):
		os.makedirs(tarx_path)
	tarx =tarfile.open(filename)
	names=tarx.getnames()
	for name in names:
		tarx.extract(name,path=tarx_path)
	tarx.close()


#tar -cvf
def tar_files(source_file_path,target_file_name):

	if not os.path.exists(source_file_path):
		return False

	dir = source_file_path
	f=tarfile.open(target_file_name,"w");

	#f=tarfile.op.ZipFile(target_file_name,'w',zipfile.ZIP_DEFLATED)
	os.chdir(source_file_path)
	for dirpath , dirnames , filenames in os.walk(dir):
		#print("dirpath:%s , dirnames%s ,filenames %s" %(dirpath,dirnames,filenames))

		for filename in filenames:
			tar_dir = "./"+dirpath[len(source_file_path):]
			#print("filename:"+filename)
			if(filename != target_file_name):
				#print("path:"+os.path.join(tar_dir,filename))
				f.add(os.path.join(tar_dir,filename))
				#f.write(os.path.join(dirpath,filename),os.path.join(tar_dir,filename))

	f.close()

def str_strip(str):

	result = str.strip()
	result = result.lstrip(" ")
	result = result.rstrip(" ")
	result = result.strip()
	return result

def change_user(user_name):

	import pwd
	user=pwd.getpwnam(user_name)


	os.setgid(user.pw_gid)
	os.setuid(user.pw_uid)
	os.environ["HOME"]=user.pw_dir
	os.environ["SHELL"]=user.pw_shell

def remove_more_space(str_obj):

	str_word=str(str_obj)
	if str_word==" ":
		return " "
	str_list=str_word.strip().split(" ")
	tmp_list=list()
	for s in str_list:
		if s!="":
			tmp_list.append(s)
	ret=""
	for s in tmp_list:
		ret=ret+s+" "
	return ret

def replace_str_by_pattern(source_str,matched_pattern,replace_str):

	result=""
	match_str=str(source_str)
	while True:
		match_re=re.search(matched_pattern,match_str)
		if match_re is None:
			break
		else:
			matched_str=match_re.group()

		pos=match_str.find(matched_str)
		result=result+match_str[0:pos]+replace_str
		match_str=match_str[pos+len(matched_str):]
	result=result+match_str
	return result


def get_md5_value(full_file_name):
	global BLOCK_SIZE
	md5_file = open(full_file_name, 'r')

	md5 = hashlib.md5()

	while True:
		data = md5_file.read(BLOCK_SIZE)
		if not data:
			break
		md5.update(data)

	md5_file.close()
	return str(md5.hexdigest()).lower()

def popen(command):
	"""
	执行shell命令
	:param command:
	:return: (recode,stdout,stderr) recode是shell命令的退出码，stdout是shell命令的标准输出，stderr是shell命令的错误输出
	"""
	new_env=os.environ.copy()
	new_env['MEGAVARIABLE'] = 'MEGAVALUE'
	p = subprocess.Popen(command,shell=True,bufsize=0,stdout=subprocess.PIPE,\
	                     stderr=subprocess.PIPE,close_fds=True,stdin=subprocess.PIPE,env=new_env)
	stdout,stderr = p.communicate()
	ret = (p.returncode,stdout,stderr)
	return ret


def load_yaml(filename):
	import yaml
	with open(filename,"r") as f:
		return yaml.load(f)

def dump_yaml(yaml_object,filename):
	import yaml
	with open(filename,"w") as f:
		f.write(yaml.dump(yaml_object))
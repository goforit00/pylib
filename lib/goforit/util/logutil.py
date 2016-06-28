__author__ = 'junqingfjq'

import sys
import os
import time


from xdeploy.util import function_util
default_log_path = "/home/admin/logs/"

def LOG_ERROR(file_name, file_def, def_num, message, exception_info = "",console=True,log_path=default_log_path,prominent=True):
	prominentErrBegin="********************ERROR-BEGIN********************\n"

	prominentErrEnd="********************ERROR---END********************\n"
	if prominent==True:
		os.system('echo "%s"'%prominentErrBegin)
	LOG_MESSAGE("ERROR", file_name, file_def, def_num, message, exception_info,console=console,log_path=log_path)
	if prominent==True:
		os.system('echo "%s"'%prominentErrEnd)

def LOG_INFO(file_name, file_def, def_num, message, exception_info = "",console=True,log_path=default_log_path):

	LOG_MESSAGE("INFO", file_name, file_def, def_num, message, exception_info,console=console,log_path=log_path)


def LOG_MESSAGE(status, file_name, function_name, line_num, message, exception_info = "",console=True,log_path=default_log_path):
	pass
	current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

	user_name=function_util.get_username_by_userid()

	log_name = user_name+"-"+current_date+".log"

	if not os.path.exists(log_path):
		try:
			os.makedirs(log_path)
			os.system("chown admin:admin /home/admin/logs")
			os.system("chmod 777 "+log_path)
			function_util.xprint("INFO: " + current_date + " " + __file__ + " " + sys._getframe().f_code.co_name + \
			      " " + str(sys._getframe().f_lineno) + " mkdir " + log_path + " success")
		except Exception, e:
			function_util.xprint("ERROR: " + current_date + " " + __file__ + " " + sys._getframe().f_code.co_name + \
			      " " + str(sys._getframe().f_lineno) + " mkdir " + log_path + " failed")


	current_date_detail = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	log_file_name = log_path + log_name

	if(exception_info != ""):
		info_write ="%s %s %s %s %s %s %s"%(status,current_date_detail,file_name,function_name,line_num,message,str(exception_info))
	else:
		info_write ="%s %s %s %s %s %s"%(status,current_date_detail,file_name,function_name,line_num,message)
	info_write=function_util.remove_more_space(info_write)
	if console!=False:
		function_util.xprint(info_write)
	with open(log_file_name,'a') as f:
		f.write(info_write+"\n")
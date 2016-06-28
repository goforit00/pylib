__author__ = 'junqingfjq'

import sys

class BaseError(Exception):
	errCode=''
	errMsg=''
	errLine=0
	errScriptName=''
	type="normal"
	flag_value='null'
	sysErrorCode='101'

	def __init__(self,errMsg,errLine,scriptName):
		Exception.__init__(self)
		self.errMsg=errMsg
		self.errLine=errLine
		self.errScriptName=scriptName

	def __str__(self):
		str="{'type':%s,'errCode':%s,'errMsg':%s,'errLine':%s,'errScriptName':%s,'flag_value':%s}" % (self.type,self.errCode,self.errMsg,self.errLine,self.errScriptName,self.flag_value)
		return str

	def toJsonStr(self):
		str="{'type':%s,'errCode':%s,'errMsg':%s,'errLine':%s,'errScriptName':%s,'flag_value':%s}" % \
			(self.type,self.errCode,self.errMsg,self.errLine,self.errScriptName,self.flag_value)
		return str

class NoFileError(BaseError):
	def __init__(self,errMsg,errLine,scriptName,flag_value):
		BaseError.__init__(self,errMsg,errLine,scriptName)
		self.flag_value=flag_value
		self.errCode=BaseError.sysErrorCode+'10011'
		self.type="NoFileError"

__author__ = 'junqingfjq'


import sys

class Context:
	def __init__(self):
		self.params_dict=dict()
		pass


class BaseExecutor:
	def __init__(self):
		pass

	def validate_params(self, argvs):
		return True

	def build_params(self,argvs):
		return argvs

	def run_steps(self, argvs):
		return True

	def execute(self, argvs = ""):
		try:
			if( False == self.validate_params(argvs)):
				print("validate_params() return False")
				sys.stdout.flush()
				return False
			context = self.build_params(argvs)
			if(context == False):
				print("build_params return False")
				sys.stdout.flush()
				return False
			if (False==self.run_steps(context)):
				print("run_steps return False")
				sys.stdout.flush()
				return False
		except Exception,e:
			print(e)
			return False
		return True
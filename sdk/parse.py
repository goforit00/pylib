__author__ = 'junqingfjq'

from optparse import OptionParser

def main():
	parser=OptionParser()
	parser.add_option("-u","--update",help="xxx",action="store_true")
	parser.add_option("-c","--create",help="xxx")
	parser.add_option("-t","--test",dest="xxx",help="xxx",action="store_true")
	parser.add_option("-p","--package",help="xxx",action="store_true")
	parser.add_option("--upload",action="store_true",help="xxx")
	parser.add_option("-l","--list",action="store", help="xxx")
	parser.add_option("-v","--version",action="store_true",help="xxx")
	parser.add_option("-P","--params",help="xxx",\
					  action="append")


	(options,args)=parser.parse_args()

	if options.create:
		print("create  %s"%options.create)


	elif options.update:
		to_version=""
		if len(args)>=1:
			to_version=args[0]


	elif options.package:
		if(len(args)>0):
			param=args[0]

	elif options.upload:
		print("xxx")

	elif options.list:
		pass
	elif options.version:
		pass
	else:
		parser.print_help()



if __name__=='__main__':
	main()

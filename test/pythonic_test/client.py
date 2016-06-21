__author__ = 'junqingfjq'

import xmlrpclib
proxy=xmlrpclib.ServerProxy('http://localhost:8000/')

print(proxy.file_readerx('./pythonicTest.py'))
__author__ = 'junqingfjq'

import os




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

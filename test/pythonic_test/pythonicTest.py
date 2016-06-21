__author__ = 'junqingfjq'


def reverse_str_or_list(s):
	return s[::-1]


if __name__ == '__main__':

	name='Tim'
	langs=['AS3','Lua','C']
	info={'name':'Tim','sex':'male','age':23}
	numList=[1,2,3,4,5]


	# if name and langs and info:
	# 	print("All not null")


	# print(reverse_str_or_list(name))
	# print(langs)
	# print(langs[::-1])

	# res=" ".join(langs)
	# print(res)

	# print(sum(numList))
	# print(max(numList))
	# print(min(numList))

	# from operator import mul
	# print(reduce(mul,numList,1))

	# print([x*x for x in range(10) if x % 3 ==0 ])


	# info['workage']=info.get('workage',0)+1
	# print(info)

	# for  x in xrange(1,5):
	# 	if x==5:
	# 		print("find 5")
	# 		break
	# else:
	# 	print("not find 5")


	# a=3
	# b=2 if a>3 else 1
	# print(b)

	# for i,e in enumerate(numList,2):
	# 	print(i,e)

	# keys=['name','sex','age']
	# values=['Tim','Male',23]
	# dic=dict(zip(keys,values))
	# print(dic)

	json_data={"status": "OK", "count": 2, "results":[{"age": 27, "name": "Oz", "lactose_intolerant": True}, {"age": 29, "name": "Joe", "lactose_intolerant": False}]}
	import json
	print(json.dump(json_data,indent=2))


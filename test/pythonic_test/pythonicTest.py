__author__ = 'junqingfjq'


def reverse_str_or_list(s):
	return s[::-1]


if __name__ == '__main__':

	name='Tim'
	langs=['AS3','Lua','C']
	info={'name':'Tim','sex':'male','age':23}

	if name and langs and info:
		print("All not null")


	print(reverse_str_or_list(name))
	print(langs)
	print(langs[::-1])

# -*- coding : utf -8 -*-
import math


def product(*numbers):
	
	for test in numbers:
		if not isinstance(test,(int,float)):
			raise TypeError ("请输入数字")
		
	l = len(numbers)
	if l == 0:
		raise TypeError ("请输入数字")
	elif l == 1:
		return numbers[0]
	else:
		r = 1
		l = l -1
		while l >= 0:
			r = r*numbers[l]
			l = l -1
		return r

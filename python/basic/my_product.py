# -*- coding : utf -8 -*-
import math

def product(*numbers):

	r = 1
	l = len(numbers)
	if l == 0:
		return None
	elif l == 1:
		return numbers
	else:
		l = l -1
		while l >= 0:
			r = r*numbers[l]
			l = l -1
		return r

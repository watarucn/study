# -*- coding:utf-8 -*-
import math


def quadratic (a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError(a is not ilegal)
	if not isinstance(b,(int,float)):
		raise TypeError(b is not ilegal)
	if not isinstance(c,(int,float)):
		raise TypeError(c is not ilegal)
	if b*b-4*a*c < 0:
		print("结果是复数")
	elif b*b-4*a*c == 0:
		return (-b+math.sqrt(b*b-4*a*c))/(2*a)
	else:
		return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)

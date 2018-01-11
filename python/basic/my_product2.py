# -*- coding:utf-8 -*-


def product(*num):
	for element in num: #进行输入判断
		if not isinstance(element,(int,float,None)):
			raise TypeError("请输入数字")
	
	if len(num) == 0:
		raise ValueError("请输入1个以上的数字")
	else:
		result = 1
		for element in num:
			 result *= element
		return result
	
		

# -*- coding: utf-8 -*-


def move(n,a,b,c): #有n个盘子，从a，通过b，移动到c
	if n == 1:
		print(a, '-->', c)
	else:
		move(n-1,a,c,b)
		print(a, '-->', c)
		move(n-1,b,a,c)
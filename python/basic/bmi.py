# -*- coding: utf-8 -*-

height = float(input("请输入身高，单位为米："))
weight = float(input("请输入体重，单位为千克："))

bmi = weight / (height*height)

print("%.1f\n"%bmi)

if bmi < 18.5:
	print("你的体重过轻")
elif bmi <25:
	print("你的体重正常")
elif bmi <28:
	print("你的体重过重")
elif bmi <32:
	print("你的体重肥胖")
else:
	print("你的体重严重肥胖")

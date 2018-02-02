#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
ID = []
Income = []
try:
    for arg in sys.argv[1:]:
        temp = arg.split(':')    
        ID.append(int(temp[0]))
        Income.append(int(temp[1]))
except:
    print("Parameter Error")

for i in range(len(Income)):
    IncomeSubSocial = Income[i]*(1-0.08-0.02-0.005-0.06)

    if IncomeSubSocial < 3500:
        TaxableIncome = 0
    else:
        TaxableIncome = IncomeSubSocial -3500

    if TaxableIncome >80000:
       Tax = TaxableIncome * 0.45 -13505
    elif TaxableIncome >55000:
       Tax = TaxableIncome * 0.35 -5505
    elif TaxableIncome >35000:
       Tax = TaxableIncome * 0.30 -2755
    elif TaxableIncome >9000:
       Tax = TaxableIncome * 0.25 -1005
    elif TaxableIncome >4500:
       Tax = TaxableIncome * 0.20 -555
    elif TaxableIncome >1500:
       Tax = TaxableIncome * 0.10 -105
    else:
       Tax = TaxableIncome * 0.03

    print ("%d:%.2f"%(ID[i],IncomeSubSocial-Tax))

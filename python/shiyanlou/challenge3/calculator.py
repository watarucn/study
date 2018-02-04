#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

class Config (object):
    def __init__(self,configfile):
        self._config = self._read_config(configfile)
    def _read_config(self,filename):  
        try:
            file=open(filename)
        except:
            print("Not Found FILE")
        finally:
            file.close()

        config = {}   

        for line in file.readlines():
            temp = line.split('=')
            try:
                config[temp[0].strip()]=int(temp[1].strip())
            except:
                print("Parament Error")
        
        return config

    def get_config(self,name):
        return self._config.get(name)

    def get_SocialFax(self):
        value = self._config.values()
        n = 0        
        for val in value[2:]:
            n += val
        return n

class UserData(object):
    def __init__(self,userdatafile):
        self._data = self._read_data(userdatafile)
        self.ID = self._data.keys()
        self.Income = self._data.values()

    def _read_data(self,filename):
        try:
            file=open(filename)
        except:
            print("Not Found File")
        finally:
            file.close()

        data={}
        for line in flie.readlines():
            temp = line.split(',')
            try:            
                data[int(temp[0])]=float(temp[1])
            except:
                print("Paramen Error")

    def calc(self,JishuL,JishuH,SocialTaxRate):
        result=[]
        for n in range(len(self.ID)):

           if self.Income[n]<JishuL:
               Money = JishuL
           elif self.Income[n]>JishuH:
               Money = JishuH
           else:
               Money = self.Income[n]

           SocialTax = Money * SocialTaxRate
           IncomeSubSocial = self.Income[n]-SocialTax
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

           IncomeSubTax = IncomeSubSocial - Tax
           
           result.append('%d,%d,%2.f,%2.f,%2.f,'%(self.ID[n],self.Income[n],SocialTax,Tax,IncomeSubTax)

        return result       

if __name__ == '__main__':

    config =Config(sys.argv[1])
    user = UserData(sys.argv[2])
    money = user.calc(config.get_config(JishuL),config.get_config(JishuH),config.get_SocialTax)
    for x in money:    
        print(x)
           
        

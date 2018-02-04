#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
class Args(object):
    def __init__(self):
        self.op=[]
        self.path=[]
        self._opration()
    def _opration(self):
        n = 0
        try:
            temp = sys.argv[1:]
            for n in range(0,len(temp),2):
                self.op.append(temp[n])
                self.path.append(temp[n+1])
        except:
            print("Parament Error In Args")
    def get_path(self,opr):
        try:
            index = self.op.index(opr)
        except:
            print("Parament Error In Args")
        return self.path[index]

class Config (object):
    def __init__(self,configfile):
        self._config = self._read_config(configfile)
    def _read_config(self,filename):  
        with open(filename) as file:
            config = {}   
            for line in file.readlines():
                temp = line.split('=')
                try:
                    config[temp[0].strip()]=float(temp[1].strip())
                except:
                    print("Parament Error In Config Class")
            return config

    def get_config(self,name):
        return self._config.get(name)

    def get_SocialTax(self):
        temp = self._config
        temp.pop('JiShuL')
        temp.pop('JiShuH')
        value = temp.values()
        n = 0        
        for val in value:
            n += val
        return n

class UserData(object):
    def __init__(self,userdatafile):
        self.ID =[]
        self.Income=[]
        self._read_data(userdatafile)

    def _read_data(self,filename):
        with open(filename) as file:
            for line in file.readlines():
                temp = line.split(',')
                try:            
                    self.ID.append(int(temp[0].strip()))
                    self.Income.append(float(temp[1].strip()))
                except:
                    print("Paramen Error In UserData class")

    def calc(self,JishuL,JishuH,SocialTaxRate):
        result=[]
        for n in range(len(self.ID)):

           if self.Income[n]<JishuL:
               Money = JishuL
           elif self.Income[n]>JishuH:
               Money = JishuH
           else:
               Money = float(self.Income[n])

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
           
           result.append('%d,%d,%.2f,%.2f,%.2f\n'%(self.ID[n],self.Income[n],SocialTax,Tax,IncomeSubTax))

        return result       
def Write_Csv(path,string):
    with open(path,'a',) as file:
        file.write(string)

if __name__ == '__main__':
    args = Args()
    config =Config(args.get_path('-c'))
    user = UserData(args.get_path('-d'))

    money = user.calc(config.get_config('JiShuL'),config.get_config('JiShuH'),config.get_SocialTax())
    for x in money:    
        Write_Csv(args.get_path('-o'),x)
           
        

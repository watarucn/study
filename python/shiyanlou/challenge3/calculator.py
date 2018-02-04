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
            config[temp[0].strip()]=temp[1].strip()
        
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
        self._config = self._read_config(userdatafile)

    def _read_config(self,filename):
        try:
            file=open(filename)
        except:
            print("Not Found File")
        finally:
            file.close()

        data={}
        for line in flie.readlines():
            temp = line.split(',')
            data[temp[0]]=temp[1]

if __name__ == '__main__':

    config =Config(sys.argv[1])
    print(config.get_config('JiShuL'))
           
        

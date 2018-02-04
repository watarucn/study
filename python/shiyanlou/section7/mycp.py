#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys

def mycp(src,dst):
    with open(src,'r') as src_file:
        with open(dst,'w') as dst_file:
            dst_file.write(src_file.read())

if __name__ == '__main__':
    if len(sys.argv)==3:
        mycp(sys.argv[1],sys.argv[2])
    else:
        print("Parament Error")
        print(sys.argv[0],'srcfile dstfile')
        sys.exit(-1)
    sys.exit(0)


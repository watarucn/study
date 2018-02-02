#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def char_count(str):
    countditc={};
    for char in str:
        c=countditc.get(char)
        if c is None:
           countditc[char]=1
        else:
           countditc[char]+=1
    print(countditc)

if __name__ == "__main__":
    c = input("Enter a string:")
    char_count(c)




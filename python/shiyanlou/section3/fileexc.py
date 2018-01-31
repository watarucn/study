#!/usr/bin/env python3
# -*- coding:utf-8 -*-


filename = input("Enter the file path:")

try:
    f = open(filename)
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File Not Found")


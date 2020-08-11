# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/zamri/.spyder2/.temp.py
"""
import codecs
import re

# read rumi jawi data
f = codecs.open("rumi-jawi-unicode.txt", mode="r", encoding='utf-8')

rjDict = {}

for line in f:
    line = line.strip()
    r, j = line.split(",")
    
    if r not in rjDict:
        rjDict[r] = [j]
    else:
        rjDict[r].append(j)
        
for k in rjDict:
    print(k, rjDict[k])
    
    
    
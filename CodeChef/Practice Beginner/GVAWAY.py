# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:54:45 2020

@author: Aprameyo
"""


Solution = []
N = int(input())
for i in range(0,N):
    a,b,c = map(int,input().split())
    if(a==b):
        Solution.append(1)
    elif(a>b):
        Solution.append(0)
    else:
        Solution.append(c)
    

for i in range(0,N):
    print(int(Solution[i]))
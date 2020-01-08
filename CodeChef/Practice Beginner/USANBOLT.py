# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:54:45 2020

@author: Aprameyo
"""
import math

#Solution = []
N = float(input())
for i in range(0,N):
    f,dtb,ta,bs = map(int,input().split())
    ttig = math.sqrt(2*(f+dtb)/ta)
    tusa = f/bs
    if(tusa<ttig):
        print('Bolt')
    else:
        print('Tiger')
    

#for i in range(0,N):
#    print(int(Solution[i]))
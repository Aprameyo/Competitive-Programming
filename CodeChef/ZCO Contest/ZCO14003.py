# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:48:10 2020

@author: Aprameyo
"""

import numpy as np
Solution = []
SolSpace = []
N = int(input())
for i in range(0,N):
    temp = int(input())
    Solution.append(temp)
    
Solution_2 = sorted(Solution)

for i in range(0,N):
    Solution_2[i] = Solution_2[i]*(N-i)
    
ans = max(Solution_2)
print(ans)
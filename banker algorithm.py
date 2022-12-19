# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:33:45 2022

@author: J SRI THRISHNA
"""
import numpy as np
def check(i):
    for j in range(no_r):
        if (needed[i][j]>available[j]):
            return 0
    return 1
no_p=5
no_r=4

sequence=np.zeros((no_p),dtype=int)
visited=np.zeros((no_p),dtype=int)

allocated=np.array([[1,2,3,4],[9,8,7,4],[7,8,9,3],[0,9,7,6],[8,7,6,2]])
maximum=np.array([[1,2,3,4],[9,8,7,4],[7,8,9,3],[0,9,7,6],[8,7,6,2]])

needed=maximum-allocated

available=np.array([3,4,5,6])

count=0
while(count<no_p):
    temp=0
    for i in range(no_p):
        if(visited[i])==0:
            if(check(i)):
                sequence[count]=i
                count+=1
                visited[i]=1
                temp=1
    if(temp==0):
        break
if (count< no_p):
    print("unsafe")
else:
    print("safe")
    print(sequence)
    print(available)


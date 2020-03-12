#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:29:11 2020

@author: krishnendu
code : Python code for solving a set of linear equations using Conjugate gradient method
"""

import numpy as np
from numpy.linalg import *
xt=np.array([7.85971,0.422926408,-0.073592239,-0.540643016,0.010626163])       #the true solution 
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=float)   #the given matrix
b=np.array([1,2,3,4,5],dtype=float)
x0=np.zeros(5,dtype = float)               #the initial solution
    
r = b - np.dot(a,x0)
p = r
rs_old = np.dot(np.transpose(r), r)
k=0
    
for i in range(len(b)):
        c=np.copy(x0)
        A = np.dot(a, p)
        m= rs_old / np.dot(np.transpose(p), A)
        x0 = x0 + np.dot(m, p)
        r = r - np.dot(m, A)
        rs_new = np.dot(np.transpose(r), r)
        if np.sqrt(rs_new) < 0:
            break
        p = r + (rs_new/rs_old)*p
        rs_old = rs_new
        if np.all(abs(x0-c))<0.01 :
            break
        k+=1
print("The solution using Conjugate gradient method is :",x0)
print("The number of iterations is :",k)


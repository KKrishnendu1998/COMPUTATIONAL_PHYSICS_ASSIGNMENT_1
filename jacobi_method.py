#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:35:36 2020

@author: krishnendu
code : Python code for solving a set of linear eqautions using Jacobi method
"""
import numpy as np
from numpy.linalg import *
xt=np.array([7.85971,0.422926408,-0.073592239,-0.540643016,0.010626163])      #true solution
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=float)   #the given matrix 
b=np.array([1,2,3,4,5],dtype=float)           
x=np.array([0,0,0,0,0],dtype=float)                #initial solution 
i=0
err=0.01                #the error bound mentioned in the problem 
while np.any(abs(x-xt)>err):                     #checking the condition
   i+=1
   p=np.copy(x)
   x=np.zeros(5)
   
   for j in range(5):
       
       for k in range(5):
           if k!=j:
               x[j]=x[j]-(a[j][k]*p[k])
             
       
       x[j]=(x[j]+b[j])/a[j][j]


print("The solution by Jacobi method :",x)               #printing the solution matrix

print("The number of iteration required :",i)           #printing the iterations 
   
               
               
    
          

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:04:14 2020

@author: krishnendu

code : Python code for finding the dominant eigenvalue and eigenvector of a sqaure matrix 
"""
import numpy as np
from numpy.linalg import *
A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])        #the given matrix

C=A

x=np.array([0,1,0])                              #defining the x matrix 

y=np.array([1,1,0])                              #defining the y matrix

k=np.inner((np.dot(A,x)),y)

l=np.inner(x,y)

e_previous= float(k)
error_threshold=0.01

while True:

    A=np.dot(A,C)
    k=np.inner((np.dot(A,x)),y)
  

    e_next=float(k/l)
    
    l=k
    
    if abs(e_previous-e_next)<=error_threshold:            #checking the condition given by the problem 
        break;
    else :
        e_previous=e_next
        
print("The dominant eigenvalue is : ",e_next)  #printing the dominant eigenvalue
b=np.dot(np.dot(np.transpose(C),A),x)
print("The corresponding eigenvector is :",b/norm(b)) #printing the eigenvector corresponding to the dominant eigenvector 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:02:52 2020

@author: krishnendu
code : Python code for producing QR decomposition of a given matrix and using the decomposition find the eigenvalues of the matrix 
"""

import numpy as np
from numpy.linalg import *
A=np.array([[5,-2],[-2,8]])  #the given matrix
l=len(A.flatten())           #finding the number of elements of the given matrix
d=len(np.diag(A))            #finding the number of diagonal elements of the given matrix 
B=qr(A)                    #finding the QR decomposition of the matrix
print("the Q matrix of the QR decomposition of the given matrix is :",B[0])
print("the R matrix of the QR decomposition of the given matrix is :",B[1])


k=0
while k!=(l-d) :              #checking whether the matrix has become diagonalized or not 
    
    k=0
    B=qr(A)
   
    A=np.dot(np.dot(np.transpose(B[0]),A),B[0])

    for i in range(0, d): 
        for j in range(0,d) : 
              

            if ((i != j) and (abs(A[i][j]) <0.001)) : 
                k+=1
                
    
print("The eigenvalues of the given matrix using QR method is : ",np.diag(A))    
print("The eigenvalues of the given matrix using np.linalg.eigh is : ",eigh(A)[0])

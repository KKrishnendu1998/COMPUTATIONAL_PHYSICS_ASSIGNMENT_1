#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:04:35 2020

@author: krishnendu
code : Python code for singular value decomposition of a given matrix 
"""

#
#In this method  A real matrix of dimention(m,n) is decomposed through A=U*S*V^T , where the S is a real Diaginal matrix of dimention(m,n) and U, V are real othogonal matrics of dimention (m,m) and (n,n) respectivly
import numpy as np
import time # T measure the time of operation 
A=np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]])# the given matrix
start_time1=time.time() # start_time1 is the initial time for  SVD operation of the  matrix through numpy
U1,S1,V1=np.linalg.svd(A)       # U1,V1,S1 are the singular value decomposed  matrics using function numpy.linalg.svd
stop_time1=time.time() # the final time after SVD operation of the  matrix through numpy


print('SVD form using the function numpy.linalg.svd is : \n')
print('U1:\n',U1,'\n S1:\n',S1,'\n V1:\n',V1)

start_time2=time.time() # start_time2 is the initial time for  SVD operation of the  matrix by using python code
eigenval_1,eigenvec_1=np.linalg.eigh(np.matmul(A,np.transpose(A)))      # calculating eigenvalues and eigen vectors of A*(A^T)
eigenval_2,eigenvec_2=np.linalg.eigh(np.matmul(np.transpose(A),A))      #eigenvalues and eigen vectors of (A^T)*A
eigen1=eigenval_1.argsort()[::-1]              #sorting of arguments of the eigenvalue 1 in descending order 
eigenval_1=eigenval_1[eigen1]               #sorting the elements of eigenvalue 1 in descending order
U2=eigenvec_1[:,eigen1]                       #sorting of eigen_vectors 1 of according to the sorted eigevalues 1
eigen2=eigenval_2.argsort()[::-1]              #sorting of arguments of the eigenvalue 2 in descending order 
eigenval_2=eigenval_2[eigen2]               #sorting the elements of eigenvalue 2 in descending order
V2=eigenvec_2[:,eigen2]                       #sorting of eigen_vectors 1 of according to the sorted eigevalues 1
S2=np.matmul(np.matmul(np.transpose(U2),A),V2)
stop_time2=time.time()                       #the final time after SVD operation of the  matrix by using python code
print('SVD form using python code: \n')
print('U2:\n',U2,'\n S2:\n',S2,'\n V2:\n',V2)   # U2,V2,S2 are the singular value decomposed  matrices by using python code      
print("the singular values of the matrix using python code is :" ,eigen1)
   
print('Time required for finding the SVD of the matrix using python code  = ',(time.time()-start_time2))
print('Time required for finding svd of the matrix using numpy.linalg.svd = ',(time.time()-start_time1))
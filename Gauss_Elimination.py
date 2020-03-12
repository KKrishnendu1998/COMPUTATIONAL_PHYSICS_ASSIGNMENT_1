#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:11:06 2020

@author: krishnendu
code: solve a set of linear eqaution using numpy.linalg.solve
"""

import numpy as np
A=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])    #the given matrix
b=np.array([2,2,2])
print(np.linalg.solve(A,b))   #printing the solution

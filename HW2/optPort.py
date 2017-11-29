# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:58:25 2017

@author: roco3
"""


from cvxopt import matrix, solvers
import numpy as np


"""
with cvxopt, solve quandratic programing

min   x'Px + q'x
s.t   Gx <= h
      ax  = b
      
where x = [[x1],
           [x2],
           ...,
           [xn]], 
      P = sigma, covariance matrix n*n
      q = 0, zeros matrix n*1
      G = [[-r1, -r2, ..., -rn],
           [-1,  0, ...   ,  0],
           [ 0, -1, ...   ,  0],
           [...           , -1]]
      h = [[-r_min],
           [0],
           ...,
           [0]]
      a = [1, 1, ..., 1]
      b = 1

input: expected return, covariance, minimum return
output: cvxopt solution      

"""

def optimize_portfolio(exp_ret, cov, r_min):
    
    n = len(exp_ret)
    P = matrix(np.array(cov))
    q = matrix(np.zeros((n, 1)), tc = 'd')
    
    G = matrix(np.concatenate(
            (-np.array([exp_ret]), -np.identity(n)), 0))
    h = matrix(np.concatenate(
            (-np.ones((1,1))*r_min, np.zeros((n,1))), 0))
    
    A = matrix(1.0, (1,n))
    b = matrix(1.0)
    sol = solvers.qp(P, q, G, h, A, b)
    
    return sol


#exp_ret = 
#cov = 
#r_min = 0


def stats(x,exp_ret,cov,r_min):
    
    mu = np.dot(np.transpose(x),np.array(exp_ret))
    std = np.sqrt(np.dot(np.dot(np.transpose(x),np.array(cov)),x))
    
    return mu,std

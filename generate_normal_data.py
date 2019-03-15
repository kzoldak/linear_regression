#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:02:42 2019

@author: kimzoldak
"""


import numpy as np
import matplotlib.pyplot as plt


import os
directory = '/Users/kimzoldak/Github/linear_regression/'
os.chdir(directory)


from scipy import stats

stats.norm.rvs?




X = np.linspace(-2, 2, 100)
scatter = stats.norm.rvs(loc=0, scale=2, size=100)
Y = 2 + 3*X + scatter
plt.plot(X, Y, 'o', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2, alpha=0.75)


X = np.linspace(-2, 2, 100)
scatter = stats.norm.rvs(loc=0, scale=3, size=100)
Y = 2 + 3*X + scatter
plt.plot(X, Y, 'o', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2, alpha=0.75)





X = np.linspace(-2, 2, 100)
scatter = stats.norm.rvs(loc=0, scale=3, size=100)
Y = 2 + 3*X + scatter
plt.plot(X, Y, 'o', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2, alpha=0.75)


X = np.linspace(-2, 2, 100)
scatter = stats.norm.rvs(loc=1, scale=3, size=100)
Y = 2 + 3*X + scatter
plt.plot(X, Y, 'o', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2, alpha=0.75)


X = np.linspace(-2, 2, 100)
scatter = stats.norm.rvs(loc=2, scale=3, size=100)
Y = 2 + 3*X + scatter
plt.plot(X, Y, 'o', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2, alpha=0.75)







def generate_normal_data(mean, std, ndata):
    '''
    generate random variates from a normal distribution
    and plot the data. X-data is limited from -2 to +2.
    
    generate_normal_data(mean, std, ndata)
    
    Parameters:
    ----------
    mean: int or float, distribution mean
    std: int or float, distribution standard deviation
    ndata: int, number of random variates to create from 
            this distribution. 
    
    '''
    X = np.linspace(-2, 2, ndata)
    scatter = stats.norm.rvs(loc=mean, scale=std, size=ndata)
    Y = 2 + 3*X + scatter  # model + scatter
    plt.plot(X, Y, 'o', 
             markerfacecolor='white', 
             markeredgecolor='blue', 
             markeredgewidth=2, alpha=0.75)
    plt.show()
    


# std = 0 means no scatter
generate_normal_data(mean=0, std=0, ndata=100)

# std = 1, minor scatter
generate_normal_data(mean=0, std=1, ndata=100)


# std = 2, moderate scatter
generate_normal_data(mean=0, std=2, ndata=100)


# std = 3, large scatter
generate_normal_data(mean=0, std=3, ndata=100)


# chaning mean will change the y-axis location of the data. 
generate_normal_data(mean=0, std=1, ndata=100)
generate_normal_data(mean=1, std=1, ndata=100)
generate_normal_data(mean=2, std=1, ndata=100)




xdata = np.asarray(data.TV)

# X = np.vstack([np.ones(len(xdata)), xdata]).T
# X = np.asmatrix(X)

# OR, A BETTER SOLUTION:
X = np.matrix([ np.ones(len(xdata)), xdata ]).T  # shape(200, 2)
y = np.asarray(data.sales)

print(X.shape)            # (200, 2)
print(y.shape)            # (200, )
print(np.vstack(y).shape) # (200, 1)

beta = ((X.T * X)**-1) * X.T * np.vstack(y)
beta







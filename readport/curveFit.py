# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 16:09:27 2018

@author: Ivan
"""

import numpy as np
#from scipy import optimize
import matplotlib.pyplot as plt

#args[0] is amplitude, args[1] is frequency, and args[2] is phase shift and args[3] is DC offset
def sineFit(x, arg0, arg1, arg2, arg3):
#    return args[0]*np.sin(args[1]*x - args[2]) + args[3]
    return arg0*np.sin(np.pi*arg1*x - arg2) + arg3


#this function takes input array and fits it with harmonic fit.
#then returns parametres
def fitHarmonic(iptData):
    #get 2 values for initial guesses in optimize function
    
    mid = np.mean(iptData)
    sigma = np.std(iptData)
    
    
#    rand = np.random.choice(iptData, size = 2, replace = False)
#    diff = abs(rand[0] - rand[1])
    
#    xarray = range(len(iptData))
    # now get limits as the mean +- 10 times standard deviation
    low = (mid - 10*sigma)
    high = (mid + 10*sigma)
    
    lowArr = np.ones(len(iptData)) * low
    highArr = np.ones(len(iptData))* high
#    
#    
#    #array1, array2 = optimize.curve_fit(sineFit, xarray, a, p0 = (0.5, 1, 1, 1.5))
#    array1, array2 = optimize.curve_fit(sineFit, xarray, iptData, p0 = (diff,1,1,rand[0]))
#    
#    [arg0, arg1, arg2, arg3] = array1
##    print(array1)s
#    
#    xline = np.linspace(0, len(iptData), 200)
#    yline = sineFit(xline, arg0, arg1, arg2, arg3)
    
    plt.plot(iptData)
    plt.plot(lowArr)
    plt.plot(highArr)
    plt.show()

    return low, high


def getImage(iptData, name):
    fig = plt.figure()
    ax = fig.gca()
    
    ax.plot(iptData, label = name)
    ax.legend()
    
    plt.savefig(fname = 'pictures/{}.png'.format(name), dpi = 300, format = 'png')
    plt.close('all')
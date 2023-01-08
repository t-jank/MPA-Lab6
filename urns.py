# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:56:33 2023

@author: t-jan
"""
import random
import matplotlib.pyplot as plt
import math

n = 10 # number of urns and balls
#k = n # number of balls

def Harmonic_Number(n):
    return 0.5772156649 + math.log(n)

def balls_throw(n):
    urns=[]
    for i in range(0,n):
        urns.append(0)
    for i in range(0,n):
        random_urn = random.randint(0,n-1)
        urns[random_urn]+=1
    return max(urns)


nMin=10
nMax=10000
nStep=13
nRepeats=10

for n in range(nMin,nMax,nStep):
    summ=0
    for r in range(0,nRepeats):
        summ+=balls_throw(n)
    if n==nMin:
        plt.scatter(n,summ/nRepeats,color='k',label='simulation, 10 repeats for each n')
        plt.scatter(n, 1.9*math.log(n)/math.log(math.log(n))-1.2, color='blue',label='1.9*log(n)/loglog(n)-1.2')
    else:
        plt.scatter(n,summ/nRepeats,color='k')
        plt.scatter(n, 1.9*math.log(n)/math.log(math.log(n))-1.2, color='blue')
#plt.xlim(left=0)
#plt.xlim(right=nMax)
plt.xlabel('n')
plt.ylabel('Number of balls in biggest urn')
plt.title('Maximum load')
plt.legend()
plt.show()



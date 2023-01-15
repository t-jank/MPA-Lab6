# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:56:33 2023

@author: t-jan
"""
import random
import matplotlib.pyplot as plt
import math
import statistics

n = 10 # number of urns and balls
#k = n # number of balls

def Harmonic_Number(n):
    return 0.5772156649 + math.log(n)

def balls_throw_uniform(n):
    urns=[]
    for i in range(0,n): # tworzenie pustych urn
        urns.append(0)
    for balls in range(0,n): # rzucanie n kul do n urn jednostajnie losowo
        random_urn = random.randint(0,n-1)
        urns[random_urn]+=1
    return max(urns)  # liczba kul w urnie, która posiada najwięcej kul

def balls_throw_subset(n,d):
    # tworzenie pustych urn
    urns=[]
    for i in range(0,n):
        urns.append(0)
    for balls in range(0,n):
        #losowanie podzbioru
        subset=[]
        for ur in range(0,d):
            subset.append(-1)
        it=0
        while -1 in subset:
            random_urn = random.randint(0,n-1)
            if random_urn not in subset:
                subset[it]=random_urn
                it+=1
        # znalezienie najmniejszej urny w wylosowanym podzbiorze
        number_of_balls_in_drawn_subset=[]
        for i in range(0,d):
            number_of_balls_in_drawn_subset.append(urns[subset[i]])
        minimum = min(number_of_balls_in_drawn_subset)
        indices = [i for i, v in enumerate(number_of_balls_in_drawn_subset) if v == minimum]
        # wrzucenie tam kuli
        rndpom=random.randint(0,len(indices)-1)
        halfrandom_urn=subset[indices[rndpom]]
        urns[halfrandom_urn]+=1
    return max(urns)

def balls_throw_groups(n,d): # tu: nMin=12, nStep=12
    urns=[]
    for i in range(0,n):
        urns.append(0)
    


nMin = 10
nMax = 10000
nStep = 13
nRepeats = 10
d = 4
ox,UB_y,LB_y,EX_y,EX2_y=[],[],[],[],[]

for n in range(nMin,nMax,nStep):
    summ=0
    for r in range(0,nRepeats):
      #  summ+=balls_throw_uniform(n)
        summ+=balls_throw_subset(n,d)
    if n==nMin:
        plt.scatter(n,summ/nRepeats,color='k',label='simulation, '+str(nRepeats)+' repeats for each n')
    else:
        plt.scatter(n,summ/nRepeats,color='k')
    ox.append(n)
    EX_y.append(1.0165*math.log(math.log(n)))
    EX2_y.append(math.log(math.log(n))/math.log(d)+0.6)
    '''    
    UB_y.append(3*math.log(n)/math.log(math.log(n)))
    LB_y.append(math.log(n)/math.log(math.log(n)))
    EX_y.append(1.577*math.log(n)/math.log(math.log(n)))
plt.plot(ox, UB_y, color='crimson',label='UB = 3*log(n)/loglog(n)',linewidth=2.5)
plt.plot(ox,EX_y, color='b',label='1.577*log(n)/loglog(n)',linewidth=3.5)
plt.plot(ox, LB_y, color='orangered',label='LB = log(n)/loglog(n)',linewidth=2.5)
'''
plt.plot(ox,EX_y, color='b',label='1.0165*loglog(n)',linewidth=2.5)
plt.plot(ox,EX2_y, color='limegreen',label='loglog(n)/log(d)+0.6',linewidth=1.5)
#plt.xlim(left=0)
#plt.xlim(right=nMax)
plt.xlabel('n')
plt.ylabel('Number of balls in biggest urn')
plt.title('Maximum load, '+str(d)+' subsets')
plt.legend()
plt.show()

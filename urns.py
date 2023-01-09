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

def balls_throw_groups(n,d):
    urns=[]
    for i in range(0,n):
        urns.append(0)
    


nMin = 10
nMax = 1000
nStep = 13
nRepeats = 10
d = 2

for n in range(nMin,nMax,nStep):
    summ=0
    for r in range(0,nRepeats):
        #summ+=balls_throw_uniform(n)
        summ+=balls_throw_subset(n,d)
    if n==nMin:
        plt.scatter(n,summ/nRepeats,color='k',label='simulation, 10 repeats for each n')
   #     plt.scatter(n, 1.9*math.log(n)/math.log(math.log(n))-1.2, color='blue',label='1.9*log(n)/loglog(n)-1.2')
    else:
        plt.scatter(n,summ/nRepeats,color='k')
 #       plt.scatter(n, 1.9*math.log(n)/math.log(math.log(n))-1.2, color='blue')
#plt.xlim(left=0)
#plt.xlim(right=nMax)
plt.xlabel('n')
plt.ylabel('Number of balls in biggest urn')
plt.title('Maximum load')
plt.legend()
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:56:33 2023

@author: t-jan
"""
import random

n = 10 # number of urns
k = n # number of balls

urns=[]
for i in range(0,n):
    urns.append(0)

for i in range(0,k):
    random_urn = random.randint(0,n-1)
    urns[random_urn]+=1



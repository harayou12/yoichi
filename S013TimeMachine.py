#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
n = input()
input_first = input()
first = []
for ki in range(2):
    first = input_first.rstrip().split(' ')
c_f = first[0]
c_b = first[1]
a = input()
result = []
cost = 0
b = []
for ii in range(int(n)):
    b.append(ii)
print(b)
while len(a) >= 0:
    for i in range(len(b)-1,0):
        if a[i] == "d":
            for k in range(i+1,len(a)-1):
                c = a[:k-1]
                if a[k+1] == "d":
                    c += "s"
                else:
                    c += "d"
            cost += 10000
            a = c
            del b[i]
        elif a[i] == "s":
            for k in range(i+1,len(a)-1):
                c = a[:k-1]
                if a[k+1] == "d":
                    c += "s"
                else:
                    c += "d"
            cost += 10
            a = c
            del b[i]
print(cost)
print(b)

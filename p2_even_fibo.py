#!/usr/bin/env python3
def getFibos(num):
    summ=0
    curr=prev=2
    prev2=0
    fiboNum=2
    while(fiboNum<num):
        summ+=fiboNum        
        fiboNum=(prev*4)+prev2
        prev2=prev
        prev=fiboNum
    return summ
t=int(input())
for i in range(t):
    n=int(input())
    print(getFibos(n))


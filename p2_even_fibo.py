#!/usr/bin/env python3
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
sqrt5=math.sqrt(5)
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


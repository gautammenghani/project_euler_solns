def getMultiples(n):
    lastThree = 3 * (n//3)
    lastFive = 5 * (n//5)
    lastFifteen = 15 * (n//15)
    threeSum= ((n//3)*(3 + lastThree))//2
    fiveSum= ((n//5)*(5 + lastFive))//2
    fifteenSum= ((n//15)*(15 + lastFifteen))//2
    return (threeSum + fiveSum-fifteenSum)
    
t=int(input())
for i in range(t):
    n=int(input())
    print(getMultiples(n-1))
    

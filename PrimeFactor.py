import math
allFactors = []
primeList = []
def factors(x) :
    print(x)
    i = 1
    while i <= x/2 :
        if (x % i==0) :
            allFactors.append(i)
        i = i + 1
    print("Done Factoring")
##factors(600851475143)
factors(2000)
for n in allFactors:
    a = 1
    y = math.sqrt(n)
    localPrime=0
    while a <= n:
        if n % a == 0:
            localPrime = localPrime + 1
        a = a+1
    if localPrime != 0:
        primeList.append(n)
        print("Found a prime")
print("Found all primes")
z = len(primeList)
z = z-1
print(primeList[z])

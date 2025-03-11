import math

def isPrime(x: int):
    global primesFound
    sqrt = math.sqrt(x)
    
    for prime in primesFound:
        if prime > sqrt: break
        
        if x % prime == 0:
            return False
        
    
    return True

primesFound = [2, 3, 5, 7]
pSum = 17
n = 8

while n < 2000000:
    if isPrime(n):
        pSum += n
        primesFound.append(n)
    n += 1

print(pSum)

# def isprime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# x = 3
# counter = 2
# while counter <= 10001:
#     if isprime(x):
#         counter += 1
#         x += 2
#     else:
#         x += 2
# print (x)


def isPrime(x: int):
    global primesFound
    
    for prime in primesFound:
        if x % prime == 0:
            return False
    
    return True

primesFound = [2, 3, 5, 7]
n = 8

while len(primesFound) != 10001:
    if isPrime(n):
        primesFound.append(n)
    n += 1

print(primesFound[-1])




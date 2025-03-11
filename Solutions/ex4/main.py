def isPalindrome(x: int):
    temp = x
    rev = 0
    
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp = temp // 10
    
    return rev == x



i = 999
j = 0
possibleNums = []

while i > 0:
    j = i
    while j > 0:
        num = i * j
        if (isPalindrome(num)):
            possibleNums.append(num)
            break
        j -= 1
        
    i -= 1

print(max(possibleNums))
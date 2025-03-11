def product(s):
    mult = 1
    for c in s:
        mult *= int(c)
    
    return mult

txt = open("src/inputs/ex8.txt").read().replace("\n", "")
i = 0
maxMult = 0

while i < len(txt) - 12:
    maxMult = max(maxMult, product(txt[i:i+13]))
    i += 1

print(maxMult)

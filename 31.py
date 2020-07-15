# find greatest common divisor or HCF
def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

# Alternative way using recurssion

def computeGcd(x, y):
    if y == 0:
        return x
    else:
        return computeGcd(y, x % y)

print(gcd(12, 17))
print(gcd(4, 6))
print(computeGcd(4, 6))

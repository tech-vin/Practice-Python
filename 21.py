# find odd or even

def isOdd(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(isOdd(2))
print(isOdd(1))
print(isOdd(-2))
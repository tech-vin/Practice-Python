def computeNumbers(a, b, c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a + b + c



print(computeNumbers(3, 5, 6))
print(computeNumbers(3, 3, 3))
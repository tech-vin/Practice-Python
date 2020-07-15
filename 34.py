def sumofnumbers(a, b):
    sum = a + b
    if sum in range(15, 21):
        return 20
    else:
        return sum

print(sumofnumbers(15, 1))
print(sumofnumbers(3, 2))
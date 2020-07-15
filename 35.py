def checkSum(a, b):
    if a == b or abs(a-b) == 5 or a + b == 5:
        return True
    else:
        return False

print(checkSum(4, 5))
print(checkSum(5, 5))
print(checkSum(10, 5))
print(checkSum(0, 5))
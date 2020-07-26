def findCube(num):
    res = 0 
    for i in range(num):
        res += i ** 3
    return res
print(findCube(8))
print(findCube(3))
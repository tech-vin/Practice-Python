# apple, 2 ==> apple apple

def copies(str, n):
    result = ''
    if n >= 0:
        for i in range(n):
            result += str + ' '
        return result
    else:
        return 'Can\'t be negative'


print(copies('apple', 3))
print(copies('grapes', 0))
print(copies('banana', -2))
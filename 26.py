'''
[2,4,3,5]
@@
@@@@
@@@
@@@@@

'''
def histogram(number):
    empty = ''
    for num in number:
        empty += num * '@' + '\n'
    return empty



print(histogram([2,4,3,5,6]))
print(histogram([2,5,7,4,8,1]))
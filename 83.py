# test whether all numbers of a list is greater than a certain number.

def check_if_greater(num, n):
    return all(x > n for x in num)


print(check_if_greater([5,8,9],  4))
print(check_if_greater([5, 8, 9], 7))
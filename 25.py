def find_value(values, value):
    if value in values:
        return True
    else:
        return False

print(find_value([2,4,1,4,2,3], 3))
print(find_value([1,2,3,4], -1))

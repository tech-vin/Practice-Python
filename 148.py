def max_min(num):
    max_num = num[0]
    min_num = num[0]

    for n in num:
        if n < max_num:
            max_num = n
            
        elif n > min_num:
            min_num = n

    return min_num, max_num


print(max_min([5,32,5,9,6,23,12,5,476,3,45,89]))



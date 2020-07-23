def positive_numbers(n):
    positive = []
    for i in n:
        if i >= 0:
            positive.append(i)
        else:
            pass
    return positive

print(positive_numbers([-1, 2, 5, -9]))


# alternative way

num = [-1, 2, 54, -2]
p = list(filter(lambda x: x > 0, num))
print(p)
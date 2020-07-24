import collections

num = [2,4,2,5,8,9,12,4]

print(sum(collections.Counter(num).values()))
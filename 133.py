from timeit import timeit

start = timeit()
sum(range(10))
end = timeit()

print(start - end)
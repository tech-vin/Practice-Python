def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l
            break

print(lcm(4, 6))
print(lcm(6, 4))
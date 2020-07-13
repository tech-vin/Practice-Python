def check(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <=100)
       


print(check(900))
print(check(800))
print(check(1900))
print(check(2100))
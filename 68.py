def sum_digits(n):
    t = 0
    while n > 0:
        r = n % 10          
        t = t + r      
        n = n // 10         
    return print(t)

sum_digits(23453)   
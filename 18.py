def sum_of_numbers(n1,n2,n3):
    sum = n1 + n2 + n3
    
    if n1 == n2 == n3:
        sum *= 3
    
    return sum

print(sum_of_numbers(1,4,7))
print(sum_of_numbers(4,4,4))
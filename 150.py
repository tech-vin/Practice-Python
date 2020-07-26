def odd_product(num):
    res = 0
    for i in range (len(num)):
        for j in range (len(num)):
            if i != j:
                res = num[i] * num[j]
                if product & 1:
                 return True
                 return False
                    
    
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
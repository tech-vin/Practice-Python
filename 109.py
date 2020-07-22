# check if number is positive, negative or zero

n = int(input('Enter No: '))
if n < 0:
    r = 'Negative'
elif n > 0:
    r = 'Positive'
elif n == 0:
    r = 'zero'
else:
    r = 'invalid input'

print(r)
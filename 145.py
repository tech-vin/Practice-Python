# x = [1,2,3]
#x = (1,2,4)
x = {3,5,7,3}

if type(x) is list:
    print('x is list')
elif type(x) is tuple:
    print('x is tuple')
elif type(x) is set:
    print('x is set')
else:
    print('x is special one')
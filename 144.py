v = 'string'
t = 12

try:
    int(v)
except:
    print('variable is string')


try:
    int(t)
    print('variable is integer')
except:
    print('variable is string')
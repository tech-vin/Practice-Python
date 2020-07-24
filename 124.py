import sys

x = 10
y = 10   # 11

if hex(id(x)) == hex(id(y)):
    print('both variables have same value')
else:
    print('both variables have different value')
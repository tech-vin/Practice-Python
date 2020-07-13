def check(str):
    if str[0:2]=='is':
        return str
    else:
        return 'is'+str

print(check('apple'))
print(check('islam'))
# inputs => str, n
# condtion =>  if str < 2 = print(str*n) else print(str[:2]*n)
# example: 'vineet', 2 => vivi 
#  example: 'v', 2 => vv

def substring_copy(str, n):
    if len(str) < 2:
        return print(str * n)
    else:
        return print(str[:2] * n)

substring_copy('vineet', 2)
substring_copy('v', 3)

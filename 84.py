# count the number occurrence of a specific character in a string


ch = 'vineet'
srch = 'e'
count = 0
for c in ch:
    if c == srch:
        count += 1
print(count) 

# alternative way

print(ch.count('e'))
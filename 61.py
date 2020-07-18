# covert feet to inch, yard mile
# inch = feet * 12  |  yard = feet / 3  |  mile = feet / 5280

def inch(feet):
    return print('inch: ',feet * 12)

def yard(feet):
    return print('yard: ',feet/3.0)

def mile(feet):
    return print('miles: ',feet/5280.0)


feet = int(input('Enter Distance: '))
inch(feet)
yard(feet)
mile(feet)

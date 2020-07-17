# feet + inches  to centimeter

def feet_inches_to_cm(f, i):
    cm = f * 30.48 + i * 2.54
    return cm

print(feet_inches_to_cm(5, 3))
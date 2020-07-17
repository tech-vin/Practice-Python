# find hypotenous of right angle triangle
import math

def hypotenous_calculator(side1, side2):
    side3 = side1 ** 2 + side2 ** 2
    return math.sqrt(side3)
    
print(hypotenous_calculator(10, 20))
# find distance between (x1, y1) & (x2, y2)
import math
def find_Distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


print(find_Distance(4, 0, 6, 6))

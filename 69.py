# sort 3 integers without using conditional statement or loops

def sorting(n1, n2, n3):
    s = min(n1, n2, n3)
    b = max(n1, n2, n3)

    srt = (n1 + n2 + n3) - b -s

    return print(s, srt, b)

sorting(2, 4, 5)
sorting(6, 4, 5)
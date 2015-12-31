def getNext(n):
    c = n
    c0 = 0
    c1 = 0

    while c & 1 == 0 and c > 0:
        c0 += 1
        c >>= 1

    while c & 1:
        c1 += 1
        c >>= 1

    if c1 == 0:
        return -1

    return n + (1 << c0) + (1 << (c1 - 1)) - 1

def getPrev(n):
    c = n
    c0 = 0
    c1 = 0

    while c & 1:
        c1 += 1
        c >>= 1

    while c & 1 == 0 and c > 0:
        c0 += 1
        c >>= 1

    if c1 == 0 or c0 == 0:
        return -1

    return n - (1 << c1) - (1 << (c0 - 1)) + 1

def updateBits(n, m, i, j):
    left = ~0 << (i + j)
    right = (1 << i) - 1
    mask = left | right

    n &= mask
    m <<= i
    
    return n | m

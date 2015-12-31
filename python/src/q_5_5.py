def numBitSwapRequired(a, b):
    count = 0
    c = a ^ b

    while c != 0:
        count += 1
        c &= c - 1

    return count

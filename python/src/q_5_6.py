from sys import getsizeof

def swapOddEvenBits(n):
    even = int('0101' * getsizeof(n), 2) & n
    odd = int('1010' * getsizeof(n), 2) & n

    return even << 1 | odd >> 1


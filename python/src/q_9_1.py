cache = [1]
def countWays(n):
    if n < 0:
        return 0
    else:
        try:
            return cache[n]
        except IndexError:
            cache.append(countWays(n - 3) + countWays(n-2) + countWays(n-1))
            return cache[n]


def countWays2(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays2(n - 3) + countWays2(n-2) + countWays2(n-1)

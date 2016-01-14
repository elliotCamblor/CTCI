def __makeChange(n, denom):
    nextDenom = 0

    if denom == 25:
        nextDenom = 10
    elif denom == 10:
        nextDenom = 5
    elif denom == 5:
        nextDenom = 1
    else:
        return 1
    
    i, ways = 0, 0
    while i*denom < n:
        ways += __makeChange(n - i*denom, nextDenom)
        i += 1

    return ways

def makeChange(n):
    return __makeChange(n, 25)

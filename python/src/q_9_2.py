import math

cache = {}
def getKey(x, y):
    return "%i, %i" % (x, y)

def countWaysDP(x, y):
    if x < 0 or y < 0:
        return 0
    elif x == 0 and y == 0:
        return 1
    elif getKey(x, y) in cache:
        return cache[getKey(x,y)]
    else:
        cache[getKey(x, y)] = countWaysDP(x-1, y) + countWaysDP(x, y-1)
        return cache[getKey(x, y)]

def countWaysBinomial(x, y):
    return int(math.factorial(x + y)/(math.factorial(x)*math.factorial(y)))

#isFree is a callback function
def __getPath(x, y, path, isFree, cache):
    if x == 0 and y == 0:
        return True
    elif getKey(x, y) in cache:
        return cache[getKey(x, y)]

    success = False
    if x >= 1 and isFree(x - 1, y):
        success = __getPath(x - 1, y, path, isFree, cache)
    
    if (not success) and y >= 1 and isFree(x, y-1):
        success = __getPath(x, y - 1, path, isFree, cache)

    if success:
        path.append(getKey(x, y))
    
    cache[getKey(x, y)] = success
    return success

def getPath(x, y, isFree):
    path = []
    cache = {}
    __getPath(x, y, path, isFree, cache)
    return path

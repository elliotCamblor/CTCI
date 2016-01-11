def magicBrute(a):
    for i in range(len(a)):
        if a[i] == i:
            return i

    return -1

def __magicFast(a, start, end):
    if end < start:
        return -1

    mid = (start + end) // 2
    
    if a[mid] == mid:
        return mid
    if a[mid] < mid:
        return __magicFast(a, mid + 1, end)
    else:
        return __magicFast(a, start, mid - 1)

def magicFast(a):
    return __magicFast(a, 0, len(a) - 1)

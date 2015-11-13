def countCompression(pStr): 
    if len(pStr) < 2:
        return len(Str)
    
    lastC = pStr[0]
    count = 1
    sLength = 0
    for c in pStr[1:]:
        if c == lastC:
            count += 1
        else
            sLength += len(str(count)) + 1
            lastC = c
            count = 1

    sLength += len(str(count)) + 1
    return sLength

def compress(pStr):
    if countCompression(pStr) >= len(pStr):
        return pStr

    lastC = pStr[0]
    count = 1
    sList = []
    for c in pStr[1:]:
        if c == lastC:
            count += 1
        else:
            sList.extend([lastC, str(count)])
            count = 1
            lastC = c
    sList.extend([lastC, str(count)])
    return ''.join(sList)

if __name__ == "__main__":


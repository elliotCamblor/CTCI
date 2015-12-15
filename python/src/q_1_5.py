def countCompression(pStr): 
    if len(pStr) < 2:
        return len(pStr)
    
    lastC = pStr[0]
    count = 1
    sLength = 0
    for c in pStr[1:]:
        if c == lastC:
            count += 1
        else:
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
    str0 = "aaabbcdddd"
    assert(compress(str0) == "a3b2c1d4")
    str1 = "absndual"
    assert(compress(str1) == str1)
    str2 = 'a'
    assert(compress(str2) == str2)
    print("success")

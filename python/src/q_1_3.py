def isPermutation(s0, s1):
    if len(s0) != len(s1):
        return False

    d = {}
    for c in s0:
        d[c] = d.get(c, 0) + 1

    for c in s1:
        val = d[c] = d.get(c, 0) - 1
        if val < 0:
            return False

    return True

if __name__ == "__main__":
    str0 = "originalString"
    str1 = "rgnltigoiiaSrn"
    
    assert(isPermutation(str0, str1))
    
    str2 = 'asdasdweawsdas'

    assert(not isPermutation(str0, str2))

    print('success')

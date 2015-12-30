def getBinaryString(num):
    if num > 1 or num < 0:
        return "ERROR"
    
    slist = ['.']
    i = 0

    while num > 0 and i < 32:
        num *= 2
        if num >= 1:
            slist.append('1')
            num -= 1
        else:
            slist.append('0')

        i += 1

    if i >= 32:
        return "ERROR"
    else:
        return ''.join(slist)

    

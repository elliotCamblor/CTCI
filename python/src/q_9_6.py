def __addParen(lst, chrList, leftRem, rightRem, count):
    if leftRem == 0 and rightRem == 0:
        lst.append(''.join(chrList))
        return

    if leftRem > 0:
        chrList[count] = '('
        __addParen(lst, chrList, leftRem - 1, rightRem, count + 1)
    
    if rightRem > leftRem:
        chrList[count] = ')'
        __addParen(lst, chrList, leftRem, rightRem - 1, count + 1)

def generateParen(num):
    lst = []
    chrList = ['']*num*2
    __addParen(lst, chrList, num, num, 0)
    return lst

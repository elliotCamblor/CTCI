import copy

def __getSubsets(wholeSet, index):

    allSubsets = []

    if index == len(wholeSet):
        allSubsets.append([])
    else:
        allSubsets = __getSubsets(wholeSet, index + 1)
        moreSubsets = copy.deepcopy(allSubsets)
        for subset in moreSubsets:
            subset.append(wholeSet[index])

        allSubsets.extend(moreSubsets)

    return allSubsets
        

def getSubsets(wholeSet):
    return __getSubsets(wholeSet, 0)

def getSubsets2(wholeSet):
    allSubsets = []
    maxK = 1 << len(wholeSet)

    for k in range(maxK):
        allSubsets.append(__getSetFromInt(wholeSet, k))

    return allSubsets

def __getSetFromInt(arr, k):
    subset = []
    i = 0
    while k:
        if k & 1 == 1:
            subset.append(arr[i])
        i += 1
        k >>= 1

    return subset

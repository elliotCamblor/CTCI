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

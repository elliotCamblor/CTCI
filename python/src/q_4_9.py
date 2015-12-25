import copy

def __findSums(node, requiredSum, path, results):
    if node == None:
        return

    sum = 0
    path.append(node.key)
        
    for i in range(len(path) - 1, -1, -1):
        sum += path[i]
        if sum == requiredSum:
            results.append(path[i:])

    __findSums(node.left, requiredSum, path, results)
    __findSums(node.right, requiredSum, path, results)
    path.pop()

def findSums(root, sum):
    results  = []
    __findSums(root, sum, [], results)
    return results

def getPerms(string):
    if not string:
        return ['']
    
    perms = []
    c = string[0]
    smallPerms = getPerms(string[1:])
    
    for smallPerm in smallPerms:
        for i in range(len(smallPerm) + 1):
            perms.append(smallPerm[:i] + c + smallPerm[i:])

    return perms

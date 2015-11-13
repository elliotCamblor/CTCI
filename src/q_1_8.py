#instead of isSubstring(), use the "in" operator
def isRotation(s1, s2):
    s1 += s1
    return s2 in s1

if __name__ == "__main__":
    print(isRotation("waterbottle", "erbottlewat"))

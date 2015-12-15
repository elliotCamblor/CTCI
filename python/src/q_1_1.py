def isUniqueASCII(str):
    if len(str) > 256:
        return False

    tracker = [False]*256
    for c in str:
        i = ord(c)
        if tracker[i]:
            return False

        tracker[i]=True

    return True

if __name__ == "__main__":
    print(isUniqueASCII("zxcvbnmasdfghjklqwertyuiop"))

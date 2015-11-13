def replaceSpaces(stringWithSpace):
    newCharList = []
    for c in stringWithSpace:
        if c == ' ':
            newCharList.append('%20')
        else:
            newCharList.append(c)

    return ''.join(newCharList)

if __name__ == "__main__":
    testSentence = "fill the spaces in this!"
    print(testSentence)
    print(replaceSpaces(testSentence))

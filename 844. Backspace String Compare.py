s = "xywrrmp"
t = "xywrrmu#p"

lastS = len(s) - 1
lastT = len(t) - 1


def getValidCharacterIndex(str, last):
    backSpaceCount = 0
    while last >= 0:
        if str[last] == "#":
            backSpaceCount += 1
        elif backSpaceCount > 0:
            backSpaceCount -= 1
        else:
            break
        last -= 1
    return last


while lastS >= 0 or lastT >= 0:
    indexS = getValidCharacterIndex(s, lastS)
    indexT = getValidCharacterIndex(t, lastT)
    if indexT < 0 and indexS < 0:
        print(True)
        break
    if indexT < 0 or indexS < 0:
        print(False)
        break
    if s[indexS] != t[indexT]:
        print(False)
        break
    lastS = indexS - 1
    lastT = indexT - 1
print(True)

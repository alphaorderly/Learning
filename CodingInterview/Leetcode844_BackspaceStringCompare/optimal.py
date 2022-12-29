def backspaceCompare(s, t):
    sPointer = len(s) - 1
    tPointer = len(t) - 1
    sSharp = 0
    tSharp = 0
    while True:
        if s[sPointer] == '#' and sPointer >= 0:
            sSharp += 1
            sPointer -= 1
            continue
        if sSharp != 0 and sPointer >= 0:
            sSharp -= 1
            sPointer -= 1
            continue
        if t[tPointer] == '#' and tPointer >= 0:
            tSharp += 1
            tPointer -= 1
            continue
        if tSharp != 0 and tPointer >= 0:
            tSharp -= 1
            tPointer -= 1
            continue
        if sPointer < 0 or tPointer < 0: break
        if s[sPointer] != t[tPointer]:
            return False
        else:
            sPointer -= 1
            tPointer -= 1

    if sPointer == -1 and tPointer == -1:
        return True
    else:
        return False


print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))


print(backspaceCompare("a##c", "#a#c"))

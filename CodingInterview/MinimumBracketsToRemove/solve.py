def minimumBracket(s: str):
    stck = list()
    lst = list(s)
    for idx in range(len(s)):
        if s[idx] == '(':
            stck.append(idx)
        elif s[idx] == ')' and len(stck) != 0:
            stck = stck[:len(stck)-1]
        else:
            lst[idx] = ''
    while len(stck) != 0:
        lst[stck[len(stck)-1]], stck = '', stck[:len(stck)-1]
    return ''.join(lst)

print(minimumBracket('))(('))
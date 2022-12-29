def backspaceCompare(s: str, t: str):
    # s 문자열의 계산
    for ch in s:
        if ch == '#' and s.index('#') != 0:
            s = s[:s.index('#')-1] + s[s.index('#')+1:]
        elif ch == '#' and s.index('#') == 0:
            s = s[:s.index('#')] + s[s.index('#')+1:]
            
    # t 문자열의 계산
    for ch in t:
        if ch == '#' and t.index('#') != 0:
            t = t[:t.index('#')-1] + t[t.index('#')+1:]
        elif ch == '#' and t.index('#') == 0:
            t = t[:t.index('#')] + t[t.index('#')+1:]

    # 문자열 비교
    return s == t

print(backspaceCompare("a##c", "#a#c"))




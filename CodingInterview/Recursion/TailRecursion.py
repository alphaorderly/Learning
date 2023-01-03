def normal(i):
    if i <= 1: return 1
    return i * normal(i-1)

def tail(i, val=1):
    if i <= 1: return val
    return tail(i-1, val * i)

print(normal(4))
print(tail(4)) 
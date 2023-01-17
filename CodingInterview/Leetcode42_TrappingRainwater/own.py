def trapping(rains):
    maxHeight = max(rains)
    water = 0
    for i in range(0, maxHeight):
        temp = list()
        for j in rains:
            if i < j:
                temp.append(1)
            else:
                temp.append(0)
        for j in range(0, len(rains)):
            if temp[j] != 1: temp[j] = 2
            else: break
        for j in range(len(rains)-1, 0, -1):
            if temp[j] != 1: temp[j] = 2
            else: break
        for j in range(0, len(rains)):
            if temp[j] == 0: water += 1
    return water

print(trapping([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))



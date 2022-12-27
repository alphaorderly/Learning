def trapping(rains):
    maxHeight = max(rains)
    water = 0
    for i in range(0, maxHeight):
        temp = list()
        for j in rains:
            if i <= j:
                temp.append(1)
            else:
                temp.append(0)
        print(temp)



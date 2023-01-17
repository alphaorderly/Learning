def trapping(rains):
    water = 0
    for i in range(1, len(rains)-1):
        lMax = max(rains[:i])
        rMax = max(rains[i+1:])
        if lMax == 0 or rMax == 0 or min(lMax, rMax) - rains[i] < 0: continue
        water += min(lMax, rMax) - rains[i]
    return water

print(trapping([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))



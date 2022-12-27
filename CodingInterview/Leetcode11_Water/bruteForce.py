def water(heights):
    max = -1
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            square = min(heights[i], heights[j]) * (j - i)
            if max < square:
                max = square
    return max

print(water([4, 6, 3, 1, 8]))
def water(heights):
    a = 0
    b = len(heights)-1
    maximal = -1

    # 두 선이 겹치기 직전까지
    while a != b:
        # 현재 두 선의 너비를 계산 한 후 최댓값을 갱신한다.
        space = min(heights[a], heights[b]) * (b - a)
        if maximal < space:
            maximal = space

        # 최솟값이 위치하는 쪽을 안쪽으로 한칸 보낸다.
        if heights[a] < heights[b]:
            a += 1
        else:
            b -= 1
    return maximal

print(water([4, 6, 3, 1, 8]))
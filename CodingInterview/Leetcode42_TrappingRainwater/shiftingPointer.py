def trapping(rains):
    water = 0
    # 포인터 위치
    left = 0
    right = len(rains) - 1

    # max값
    maxLeft = 0
    maxRight = 0


    while left != right:

        # 값이 작은쪽이 안쪽으로 이동
        if rains[left] < rains[right]:

            # 자신의 값이 max값보다 크다면 -> max에 대입하고 안쪽 이동
            if maxLeft <= rains[left]:
                maxLeft = rains[left]
                left += 1

            # 자신의 값이 max보다 작다면 -> 반대쪽 max는 자기쪽 max보다 큰것은 확실하기에, 
            # 자신의 max값이 곧 양쪽 벽 최댓값 둘중 작은 값임. 
            # 이 값에 자신의 높이를 빼준 값을 총 water에서 빼줌
            else:
                water += maxLeft - rains[left]
                left += 1

        # 반대편은 그냥 변수명만 바꿔주면 됨.
        else:
            if maxRight <= rains[right]:
                maxRight = rains[right]
                right -= 1
            else:
                water += maxRight - rains[right]
                right -= 1
    return water


print(trapping([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))



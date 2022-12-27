def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]

print(twoSum([2, 7, 11, 15], 9))
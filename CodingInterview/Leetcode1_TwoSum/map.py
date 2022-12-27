def twoSum(numbers, target):
    d = dict()
    for i in range(len(numbers)):
        if numbers[i] in d:
            return [d[numbers[i]], i]
        else:
            d[target - numbers[i]] = i

print(twoSum([2, 7, 11, 15], 9))
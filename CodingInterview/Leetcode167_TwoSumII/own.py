from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for (i, v) in enumerate(numbers):
            if v in dct:
                return [dct[v]+1, i+1]
            else:
                dct[target-v] = i
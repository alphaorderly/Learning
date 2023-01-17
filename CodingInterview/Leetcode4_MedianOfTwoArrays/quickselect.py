from typing import List
import random


def quick(lst, start, end):
    pivotValue = lst[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= end and lst[i] < pivotValue:
            i += 1
        while j > 0 and lst[j] > pivotValue:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i, j = i+1, j-1
    lst[start], lst[j] = lst[j], lst[start]
    return j

def findIndex(lst, index):
    start = 0
    end = len(lst)-1
    while start <= end:
        p = quick(lst, start, end)
        if p == index: return lst[p]
        elif p > index:
            end = p - 1
        else:
            start = p + 1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2

        if len(nums) % 2 == 0:
            return (findIndex(nums, len(nums) // 2 - 1) + findIndex(nums, len(nums) // 2)) / 2
        else:
            return findIndex(nums, len(nums) // 2)

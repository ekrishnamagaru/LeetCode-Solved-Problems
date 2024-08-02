# https://leetcode.com/problems/range-sum-query-immutable/description/
# Difficulty: Easy
# Tags: Prefix

# Problem:
# Given an integer array, handle multiple queries of the following type
# 1. Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right

# Implement the NumArray class.

# Solution: O(n) time, O(n) space

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def sumRange(self, left: int, right: int) -> int:
        prefix = [0] * len(self.nums)
        runningSum = 0
        for i, num in enumerate(self.nums):
            runningSum += num
            prefix[i] = runningSum
        if left == 0:
            return prefix[right]
        else:
            return prefix[right] - prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# https://leetcode.com/problems/find-pivot-index/
# Difficulty: Easy
# Tags: Prefix, Postfix

# Problem:
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

# Solution: O(n) time
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1st Attempt
        # if len(nums) == 1: return 0
        # prefix, postfix = [0] * len(nums), [0] * len(nums)
        # runningSum = 0
        # for i in range(len(nums)):
        #     runningSum += nums[i]
        #     prefix[i] = runningSum
        # runningSum = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     runningSum += nums[i]
        #     postfix[i] = runningSum
        # for i in range(len(nums)):
        #     if i == 0:
        #         if postfix[i+1] == 0:
        #             return i
        #         else:
        #             continue
        #     if i == len(nums) - 1:
        #         if prefix[i-1] == 0: 
        #             return i
        #         else:
        #             continue
        #     if prefix[i-1] == postfix[i+1]:
        #         return i
        # return -1

        # 2nd Attempt
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

# https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Tags: Prefix

# Problem:
# Given an array of numbers, we define a running sum of an array as
# runningSum[i] = sum(nums[0]...nums[i]).
# Return the running sum of nums

# Solution: O(n) time, O(1) space
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1st Attempt:
        # runningSum = 0
        # returnArray = [0] * len(nums)
        # for i, num in enumerate(nums):
        #     runningSum += num
        #     returnArray[i] = runningSum
        # return returnArray

        # 2nd Attempt:
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums

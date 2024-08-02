# https://leetcode.com/problems/product-of-array-except-self/description/
# Difficulty: Medium
# Tags: Prefix, Postfix

# Problem:
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution: O(n) time, O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer, prefix, postfix = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        # Get prefix product
        runningProduct = 1
        for i in range(len(nums)):
            runningProduct *= nums[i]
            prefix[i] = runningProduct
        # Get postfix product
        runningProduct = 1
        for i in range(len(nums)-1, -1, -1):
            runningProduct *= nums[i]
            postfix[i] = runningProduct
        # answer[i] = (nums[0] * ... * nums[i-1]) * (nums[i+1] * ... * nums[len(nums)-1])
        # answer[i] = prefix[i-1] * postfix[i+1] (need to watch for edge cases)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = postfix[i+1]
            elif i == len(nums) - 1:
                answer[i] = prefix[i-1]
            else:
                answer[i] = prefix[i-1] * postfix[i+1]
        return answer 

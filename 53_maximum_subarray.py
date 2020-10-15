#!/usr/bin/env python3

"""
https://leetcode.com/problems/maximum-subarray

Accepted Answer: Yes
Runtime: 60ms
Memory: 14.6MB

Note:
  Most efficient solution came from using Kadane's Algorithm
    https://www.codingninjas.com/blog/2020/09/17/a-quick-look-at-kadanes-algorithm/
  .. previous attempts were O(n^2)
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cs = nums[0]
        ms = nums [0]
        for n in nums[1:]:
            cs = max(n, cs + n)
            ms = max(cs, ms)
        return ms

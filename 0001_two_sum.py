#!/usr/bin/env python3

"""
https://leetcode.com/problems/two-sum

Accepted Answer: Yes
Runtime: 44ms
Memory: 15.2MB
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            d = target - n
            if d in diff:
                return i, diff[d]
            diff[n] = i
        return None

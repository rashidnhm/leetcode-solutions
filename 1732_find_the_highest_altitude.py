#!/usr/bin/env python3

"""
https://leetcode.com/problems/find-the-highest-altitude/submissions

Accepted Answer: Yes
Runtime: 28 ms
Memory: 14.3MB
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        initial_height = 0
        max_height = initial_height
        current_height = initial_height
        for i in gain:
            current_height += i
            if current_height > max_height:
                max_height = current_height
        return max_height


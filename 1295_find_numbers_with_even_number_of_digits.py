#!/usr/bin/env python3

"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions

Accepted Answer: Yes
Runtime: 56ms
Memory: 14.4MB
"""

import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            len_n = math.ceil(math.log(n, 10))
            if n == 10**len_n:
                len_n += 1
            if len_n % 2 == 0:
                count += 1
        return count

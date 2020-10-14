#!/usr/bin/env python3

"""
https://leetcode.com/problems/zigzag-conversion

Accepted Answer: Yes
Runtime: 44ms
Memory: 14.2MB
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = ["" for _ in range(numRows)]
        counter = 0
        by_val = 1
        for i, c in enumerate(s):
            if counter == numRows - 1 or counter == 0 and i != 0:
                by_val *= -1
            lst[counter] += c
            counter += by_val
        return "".join(lst)

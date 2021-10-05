#!/usr/bin/env python3

"""
https://leetcode.com/problems/length-of-last-word

Accepted Answer: Yes
Runtime: 33ms
Memory: 14.5MB
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first_hit = False
        len_last = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] and s[i] != " ":
                first_hit = True
                len_last += 1
            else:
                if not first_hit:
                    continue
                break
        return len_last
        

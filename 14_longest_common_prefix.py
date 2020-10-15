#!/usr/bin/env python3

"""
https://leetcode.com/problems/longest-common-prefix

Accepted Answer: Yes
Runtime: 36ms
Memory: 14.3MB
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        lp = ""
        for c in strs[0]:
            tp = lp + c
            match_found = True
            for s in strs[1:]:
                if s[:len(tp)] != tp:
                    match_found = False
                    break
            if not match_found:
                break
            else:
                lp = tp
        return lp

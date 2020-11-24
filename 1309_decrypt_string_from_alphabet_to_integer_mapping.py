#!/usr/bin/env python3

"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

Accepted Answer: Yes
Runtime: 28 ms
Memory: 14.4 MB
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapped = ""
        cm = ""

        for c in s:
            if c == "#":
                l2 = cm[-2:]
                le = cm[:-2]
                for ic in le:
                    mapped += chr(96 + int(ic))
                mapped += chr(96 + int(l2))
                cm = ""
            elif len(cm) >= 3:
                mapped += chr(96 + int(cm[0]))
                cm = cm[1:] + c
            else:
                cm += c
        if cm:
            for ic in cm:
                mapped += chr(96 + int(ic))
        return mapped

#!/usr/bin/env python3

"""
https://leetcode.com/problems/decode-string

Accepted Answer: Yes
Runtime: 32ms
Memory: 14.1MB
"""

class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s

        bracket_index = s.index("[")
        num = 0
        first_half = ""
        for char in s[:bracket_index]:
            if char.isdigit():
                num *= 10
                num += int(char)
            else:
                first_half += char

        depth = 1
        for i, char in enumerate(s[bracket_index+1:], bracket_index+1):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1

            if depth == 0:
                if not num:
                    return first_half + self.decodeString(s[bracket_index+1:i]) + self.decodeString(s[i+1:])
                return first_half + num * self.decodeString(s[bracket_index+1:i]) + self.decodeString(s[i+1:])
        return s

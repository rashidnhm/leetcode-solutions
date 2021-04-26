#!/usr/bin/env python3

"""
https://leetcode.com/problems/decode-xored-array

Accepted Answer: Yes
Runtime: 224ms
Memory: 15.9MB
"""

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for i in range(len(encoded)):
            d = decoded[i]^encoded[i]
            decoded.append(d)
        return decoded

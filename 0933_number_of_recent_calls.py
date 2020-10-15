#!/usr/bin/env python3

"""
https://leetcode.com/problems/number-of-recent-calls

Accepted Answer: Yes
Runtime: 288ms
Memory: 18.87MB
"""

class RecentCounter:

    def __init__(self):
        self.__pings = []

    def ping(self, t: int) -> int:
        self.__pings.append(t)
        while self.__pings and self.__pings[0] < t - 3000: self.__pings.pop(0)
        return len(self.__pings)   


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

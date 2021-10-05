#!/usr/bin/env python3

"""
https://leetcode.com/problems/merge-intervals

Accepted Answer: Yes
Runtime: 84ms
Memory: 16.1MB
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_sorted = sorted(intervals,
                                  key=lambda x: x[0])
        intervals_len = len(intervals_sorted)

        if intervals_len == 1:
            return intervals

        merged_intervals = []
        for i in range(intervals_len):
            start = intervals_sorted[i][0]
            end = intervals_sorted[i][1]

            if not merged_intervals:
                merged_intervals.append([start, end])
                continue

            m_end = merged_intervals[-1][1]
            if m_end >= start:
                if m_end < end:
                    merged_intervals[-1][1] = end
            else:
                merged_intervals.append([start, end])

        return merged_intervals
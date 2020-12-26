#!/usr/bin/env python3

"""
https://leetcode.com/problems/minimum-time-visiting-all-points

Accepted Answer: Yes
Runtime: 60ms
Memory: 14.1MB
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        min_dist = 0

        cur_point = points[0]
        for next_point in points[1:]:
            d_delta_x = abs(next_point[0] - cur_point[0])
            d_delta_y = abs(next_point[1] - cur_point[1])

            if d_delta_x and d_delta_y:
                diag = min(d_delta_x, d_delta_y)
                if diag == d_delta_x:
                    d_delta_x = 0
                    d_delta_y -= diag
                else:
                    d_delta_y = 0
                    d_delta_x -= diag
            else:
                diag = 0

            min_dist += diag + d_delta_x + d_delta_y
            cur_point = next_point

        return min_dist

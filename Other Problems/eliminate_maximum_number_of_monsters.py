"""
Eliminate Maximum Number of Monsters
Difficulty: Medium

> https://leetcode.com/problems/eliminate-maximum-number-of-monsters

Notes:
    - Beats 18% of time submissions
"""

import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)

        t = []
        for i in range(n):
            x = dist[i] / speed[i]
            if x.is_integer():
                x -= 1
            else:
                x = math.trunc(x)
            t.append(x)
        t.sort()

        for i in range(n):
            if t[i] - i < 0:
                return i
        return i + 1


if __name__ == "__main__":
    print(Solution().eliminateMaximum([1, 3, 5], [1, 2, 3]))

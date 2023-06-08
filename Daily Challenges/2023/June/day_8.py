"""
Daily challenge for 08/06/2023
Difficulty: Easy

> https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

Notes:
    - Time taken was 4:09 minutes
    - Beats 48% of time submissions
    - Will refactor this solution in order to achieve a better time complexity
"""

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        t = 0
        for n in range(len(grid)):
            l = len(grid[n])
            for i, m in enumerate(range(l)):
                if grid[n][m] < 0:
                    t += l - i
                    break
        return t
    
if __name__ == "__main__":
    print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
"""
Daily challenge for 08/06/2023
Difficulty: Easy

> https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix

Notes:
    - Beats 70% of time submissions
"""

from typing import List


class Solution:
    def find_negative_index(self, array: List[int]):
        left = 0
        right = len(array) - 1

        # Edge cases such as no values or
        # all numbers are negative
        if not array or array[0] < 0:
            return 0

        while right + 1 > left:
            mid = (left + right) // 2
            num = array[mid]

            # Num must be negative and the index about num
            # must be greater than or equal to 0
            if 0 > num and array[mid - 1] >= 0:
                return mid

            if num >= 0:
                left = mid + 1
            else:
                right = mid - 1
        # No negative numbers so return the last index
        # of the array + 1 which is also the length
        return len(array)

    def countNegatives(self, grid: List[List[int]]) -> int:
        t = 0
        m = len(grid)
        n = len(grid[0])
        bound = n

        for i in range(m):
            bound = self.find_negative_index(grid[i][:bound])
            t += bound
        return (m * n) - t


if __name__ == "__main__":
    print(
        Solution().countNegatives(
            [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
        )
    )

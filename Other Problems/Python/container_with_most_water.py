"""
Container with most water
Difficulty: Medium

> https://leetcode.com/problems/container-with-most-water/

Notes:
    - Optimal O(n) solution using a left and a right pointer
    - Beats 43% of time submissions
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = 0
        l = 0
        r = len(height) - 1
        while l < r:
            a = (r - l) * min(height[r], height[l])
            n = max(a, n)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return n


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

"""
Daily challenge for 05/06/2023
Difficulty: Easy

> https://leetcode.com/problems/check-if-it-is-a-straight-line/

Notes:
    - Beat 40% of time submissions
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        # Edge cases
        # no slope or y-intercept (horizontal/vertical)
        if all(c[0] == x0 for c in coordinates) or all(c[1] == y0 for c in coordinates):
            return True
        # no change in x-coord
        if (x0 - x1) == 0:
            return False

        # Get straight line gradient (m = delta y / delta x)
        m = (y0 - y1) / (x0 - x1)

        for x, y in coordinates[1:]:
            if (x - x0) == 0:
                return False

            # fake gradient
            if (y - y0) / (x - x0) != m:
                return False
        return True


if __name__ == "__main__":
    print(Solution().checkStraightLine([[0, 0], [0, 1], [0, -1]]))

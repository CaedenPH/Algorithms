"""
Daily challenge for 06/06/23
Difficulty: Easy

> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

Notes:
    - Time taken was 2:04 minutes
    - Beats 43% of time submissions
    - In order to improve time complexity, the solution should be refactored
        so that the array does not need to be sorted
"""


from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        if len(arr) <= 1:
            return True

        k = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != k:
                return False
        return True


if __name__ == "__main__":
    print(Solution().canMakeArithmeticProgression([3, 5, 1]))

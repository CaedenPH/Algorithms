"""
Daily challenge for 25/07/2023
Difficulty: Medium

> https://leetcode.com/problems/peak-index-in-a-mountain-array

Notes:
    - Uses binary search (partially) to find peak 
"""


from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)

        left = 0
        right = n - 1
        # Use binary search to find peak in a
        # semi-sorted array where will focus on the
        # ascending order sorted array before the peak
        while right > left:
            mid = (right + left) // 2
            item = arr[mid]
            if (mid + 1 == n) or (mid - 1 < 0) or (item > arr[mid + 1] and item > arr[mid - 1]):
                break  # Found peak either at edge or satisfying
                # greater than neighbouring items

            if item > arr[mid - 1]:
                left = mid
            else:
                right = mid
        return mid


if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([18, 29, 38, 59, 98, 100, 99, 98, 90]))

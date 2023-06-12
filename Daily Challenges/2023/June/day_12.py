"""
Daily challenge for 11/06/2023
Difficulty: Easy

> https://leetcode.com/problems/summary-ranges

Notes:
    - Beats 68% of time submissions
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        ranges: List[List[int]] = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                # Start new range
                if not ranges or len(ranges[-1]) == 2:
                    ranges.append([nums[i] - 1])
            else:
                # End previous range and start new one
                if ranges and len(ranges[-1]) == 1:
                    ranges[-1].append(nums[i - 1])
                else:
                    ranges.append([nums[i - 1], nums[i - 1]])

        if len(ranges[-1]) == 2:
            ranges.append([nums[-1], nums[-1]])
        else:
            ranges[-1].append(nums[-1])
        return [f"{a}->{b}" if a != b else str(a) for a, b in ranges]


if __name__ == "__main__":
    print(Solution().summaryRanges([1, 3]))

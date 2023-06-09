"""
Daily challenge for 09/06/2023
Difficulty: Easy

> https://leetcode.com/problems/find-smallest-letter-greater-than-target

Notes:
    - Beat 53% of time submissions
    - Took 2 minutes
"""

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == "z":
            return letters[0]
        if target == "y" and letters[-1] != "z":
            return letters[0]

        for letter in letters:
            if letter > target:
                return letter
        return letters[0]


if __name__ == "__main__":
    print(Solution().nextGreatestLetter(["c", "f", "j"], "j"))

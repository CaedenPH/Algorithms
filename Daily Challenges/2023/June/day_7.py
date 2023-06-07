"""
Daily challenge for 07/06/2023
Difficulty: Medium

> https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/submissions/965897260/

Notes:
    - Beats 82% of time submissions
"""

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab = format(a, "b")
        bb = format(b, "b")
        cb = format(c, "b")

        m = len(max(ab, bb, cb, key=lambda m: len(m)))
        ab = ab.rjust(m, "0")
        bb = bb.rjust(m, "0")
        cb = cb.rjust(m, "0")

        n = 0
        for i in range(m):
            if cb[i] == "0":
                # No bits can be 0
                if ab[i] == "1":
                    n += 1
                if bb[i] == "1":
                    n += 1 
            else:  # cb[i] == 1
                # Both bits cannot be 0
                if ab[i] == "0" and bb[i] == "0":
                    n += 1
        return n   


if __name__ == "__main__":
    print(Solution().minFlips(8, 3, 5))
"""
String to Integer (atoi)
Difficulty: Medium

> https://leetcode.com/problems/string-to-integer-atoi

Notes:
    - Beats 50% of time submissions
"""

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        number = re.search(r"^\s*[+-]?(\d+)", s)
        if not number or not (number := number.group(1)):
            return 0

        if s.index(number) != 0 and s[s.index(number) - 1] == "-":
            number = max(0 - int(number), -(2**31))
        else:
            number = min(int(number), 2**31 - 1)
        return number


if __name__ == "__main__":
    print(Solution().myAtoi("b+-42"))

"""
Minimum Remove to Make Valid Parentheses

> https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Notes:
    - Beats 70% of time submissions
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        po = []
        pc = []
        r = lambda string, index: string[:index] + string[index + 1 :]

        for i, c in enumerate(s):
            if c == "(":
                po.append(i)
            elif c == ")":
                if po:
                    po.pop(-1)
                else:
                    pc.append(i)

        p = pc + po
        p.sort(reverse=True)

        for a in p:
            s = r(s, a)
        return s


if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))

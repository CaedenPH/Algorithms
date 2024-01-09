"""
Daily Challenge for 13/06/2023
Difficulty: Medium

> https://leetcode.com/problems/minimum-absolute-difference-in-bst

Notes:
    - Very slow O(n^2) due to finding min diff so only beats
        5% of time submssions
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recurse_all_nodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        values = [root.val]
        if root.left:
            values.extend(self.recurse_all_nodes(root.left))
        if root.right:
            values.extend(self.recurse_all_nodes(root.right))
        return values

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = self.recurse_all_nodes(root)
        min_diff = float("inf")
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if abs(values[i] - values[j]) < min_diff:
                    min_diff = abs(values[i] - values[j])
        return min_diff


if __name__ == "__main__":
    print(
        Solution().getMinimumDifference(
            TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        )
    )

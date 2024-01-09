"""
Daily Challenge for 15/06/2023
Difficulty: Medium

> https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

Notes:
    - Only beats 30% time submissions
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(
        self, node: Optional[TreeNode], levels: dict[int, list[int]], level: int
    ) -> dict[int, list[int]]:
        if not node:
            return levels

        if level not in levels:
            levels[level] = [node.val]
        else:
            levels[level].append(node.val)

        levels = self.dfs(node.left, levels, level + 1)
        levels = self.dfs(node.right, levels, level + 1)
        return levels

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = self.dfs(root, {}, 1)
        max_sum = float("-inf")
        min_level = 1
        for level, values in levels.items():
            sum_values = sum(values)
            if sum_values > max_sum:
                max_sum = sum_values
                min_level = level
        return min_level


if __name__ == "__main__":
    print(Solution().maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))

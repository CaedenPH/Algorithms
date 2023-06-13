"""
Daily Challenge for 13/06/2023
Difficulty: Medium

> https://leetcode.com/problems/equal-row-and-column-pairs

Notes:
    - Beats 40% of time submissions
"""

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns, rows = [], []
        for i in range(len(grid)):
            columns.append(','.join([str(grid[j][i]) for j in range(len(grid))]))
            rows.append(','.join(list(map(str, grid[i]))))

        number_dict = {}
        for row in rows:
            if row in columns and row not in number_dict:
                number_dict[row] = columns.count(row)
        for column in columns:
            if column in number_dict:
                number_dict[row] += rows.count(column) - 1
        return sum(list(number_dict.values()))

if __name__ == "__main__":
    print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
        
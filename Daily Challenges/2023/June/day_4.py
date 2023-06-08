"""
Daily challenge for 04/06/2023
Difficulty: Medium

> https://leetcode.com/problems/number-of-provinces

Notes:
    - Time taken was 43:28 minutes
    - Poor solution, needs to be improved
    - Should've used recursion
    - Only beats 5% of time submissions
"""

from typing import Dict, List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        connections: Dict[int, List[int]] = {}
        n = len(isConnected)

        # Group connections
        for i in range(n):
            for j in range(n):
                if i not in connections:
                    connections[i] = []
                if i != j and isConnected[i][j] == 1:
                    connections[i].append(j)

        for i in list(connections.keys()).copy():  # 0
            if i not in connections:
                continue

            cc = connections[i]  # [3]
            # Find first occurance of i
            for v in list(connections.keys()).copy():
                if i in connections.get(v, []) and i != v:
                    # Completely dump cc into this occurance
                    connections[v].extend(cc)
                    del connections[i]
                    break

            for v in cc:
                if i not in connections:
                    continue
                for j in list(connections.keys()).copy():
                    if v in connections[j] and j != i:
                        connections[j].extend(cc)
                        del connections[i]
                        break

        return len(connections)


if __name__ == "__main__":
    print(
        Solution().findCircleNum(
            [
                [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            ]
        )
    )

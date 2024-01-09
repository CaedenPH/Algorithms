"""
Daily challenge for 22/07/2023
Difficulty: Medium

> https://leetcode.com/problems/knight-probability-in-chessboard

Notes:
    - This solution fails due to time limit exceded
"""


from copy import deepcopy


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1.0

        # (x, y)
        move_perms = ((-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1))

        board = [[0 for _ in range(n)] for _ in range(n)]
        board[row][column] = 1  # Start pos (temp)

        # Iterate through each move
        for _ in range(k):  # O(k)
            new_board = deepcopy(board)
            prev = []

            for x in range(n):  # O(n * k)
                for y in range(n):  # O(n^2 * k)
                    p = board[x][y]

                    if p > 0.0:
                        for __ in range(p):  # O(n^2 * k^2) worst case
                            prev.append((x, y))
                            for move_x, move_y in move_perms:  # O(1) so discredit
                                # Increment counter if within board
                                if n > x + move_x >= 0 and n > y + move_y >= 0:
                                    new_board[x + move_x][y + move_y] += 1

            for x, y in prev:  # Ignore time complexity as its + k
                new_board[x][y] -= 1
            board = new_board
        return sum(map(lambda m: sum(m), board)) / (8**k)


if __name__ == "__main__":
    print(Solution().knightProbability(n=3, k=3, row=0, column=0))

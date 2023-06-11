"""
Daily challenge for 10/06/2023
Difficulty: Medium

> https://leetcode.com/problems/snapshot-array

Notes:
    - Time taken was 30 minutes
    - Horible time, beats 5% of time submissions - need to refactor
    - Memory beats 86% due to only holding diffs
"""


class SnapshotArray:
    def __init__(self, length: int):
        self.length = length
        self.snap_count = 0
        self.snaps = {0: {}}

    def set(self, index: int, val: int) -> None:
        self.snaps[self.snap_count][index] = val

    def snap(self) -> int:
        self.snap_count += 1
        self.snaps[self.snap_count] = {}
        return self.snap_count - 1

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if index in self.snaps[i]:
                return self.snaps[i][index]
        return 0


if __name__ == "__main__":
    obj = SnapshotArray(1)
    obj.set(0, 4)
    print(obj.get(0, 0))
    obj.set(0, 10)
    print(obj.snap())
    print(obj.get(0, 0))
    print(obj.snap())
    print(obj.get(0, 1))

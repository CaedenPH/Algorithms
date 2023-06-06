"""
Design a Number Container System
Difficulty: Medium

> https://leetcode.com/problems/design-a-number-container-system

Notes:
    - All about having the fastest possible runtime
    - Find times are O(1) constant time
    - Change times are O(log n) time due to having to use binary
        search to insert and delete
    - Beats 8.60% of time submissions
"""

from typing import Dict, List


class NumberContainers:
    def __init__(self):
        # Holds number as the key and returns list of indexes where the number is
        # The list of indexes is a sorted array in ascending order
        self.numbermap: Dict[int, List[int]] = {}
        # Simply holds each index and it's number
        self.indexmap: Dict[int, int] = {}

    def binary_search_delete(self, array: List[int], index: int) -> List[int]:
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == index:
                array.pop(mid)
                return array
            elif array[mid] < index:
                low = mid + 1
            else:
                high = mid - 1

    def binary_search_insert(self, array: List[int], index: int) -> List[int]:
        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            if array[mid] == index:
                # If the item already exists in the array, insert it after the existing item
                array.insert(mid + 1, index)
                return array
            elif array[mid] < index:
                low = mid + 1
            else:
                high = mid - 1

        # If the item doesn't exist in the array, insert it at the appropriate position
        array.insert(low, index)
        return array

    def change(self, index: int, number: int) -> None:
        # Remove previous index
        if index in self.indexmap:
            n = self.indexmap[index]
            if len(self.numbermap[n]) == 1:
                del self.numbermap[n]
            else:
                self.numbermap[n] = self.binary_search_delete(self.numbermap[n], index)

        # Set new index
        self.indexmap[index] = number

        # Number not seen before or empty so insert number value
        if not number in self.numbermap:
            self.numbermap[number] = [index]

        # Here we need to perform a binary search insertion in order to insert
        # The item in the correct place
        else:
            self.numbermap[number] = self.binary_search_insert(
                self.numbermap[number], index
            )

    def find(self, number: int) -> int:
        # Simply return the 0th index (smallest) of the indexes found (or -1)
        return self.numbermap.get(number, [-1])[0]


if __name__ == "__main__":
    obj = NumberContainers()
    print(obj.find(10))  # -1

    obj.change(2, 10)
    obj.change(1, 10)
    obj.change(3, 10)
    obj.change(5, 10)
    print(obj.find(10))  # 1

    obj.change(1, 20)
    print(obj.find(10))  # 2

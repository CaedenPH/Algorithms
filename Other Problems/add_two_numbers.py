"""
Add Two Numbers
Difficulty: Medium

> https://leetcode.com/problems/add-two-numbers

Notes:
    - Beats 60% of time submissions
    - Took 20:34 minutes
"""


from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def recurse_linked_list(self, linked_list: Optional[ListNode], numbers: List[int]) -> List[int]:
        if not linked_list:
            return numbers
        numbers.append(str(linked_list.val))
        return self.recurse_linked_list(linked_list.next, numbers)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numbers = [self.recurse_linked_list(ll, []) for ll in [l1, l2]]
        added_numbers = str(sum(int("".join(n[::-1])) for n in numbers))[::-1]

        head = ListNode(added_numbers[0])
        current_node = head
        for number in added_numbers[1:]:
            new_node = ListNode(int(number))
            current_node.next = new_node
            current_node = new_node
        return head


if __name__ == "__main__":
    print(
        Solution().addTwoNumbers(
            ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
        )
    )
    print(
        Solution().addTwoNumbers(
            ListNode(2, ListNode(4, ListNode(9))),
            ListNode(5, ListNode(6, ListNode(4, ListNode(9)))),
        )
    )

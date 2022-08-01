# Problem statement
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        new_head = head
        while head.next is not None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return new_head


# TODO: Change the tests
if __name__ == "__main__":
    input_list = [
        ListNode(1, ListNode(1, ListNode(2))),
        ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))),
    ]
    output_list = [ListNode(1, ListNode(2)), ListNode(1, ListNode(2, ListNode(3)))]
    failed_solutions = 0
    for i in range(len(input_list)):
        try:
            assert Solution().deleteDuplicates(input_list[i]) == output_list[i]
        except AssertionError:
            print(f"Test number {i} failed")
            failed_solutions += 1
    if failed_solutions == 0:
        print("All tests passed!")

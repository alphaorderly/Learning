# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        h = head
        while h != None:
            length += 1
            h = h.next
        def removal(head: Optional[ListNode], n: int):
            place = length - n
            if place == 0: return head.next
            place -= 1
            ret = head
            for i in range(place):
                head = head.next
            head.next = head.next.next
            return ret
        return removal(head, n)



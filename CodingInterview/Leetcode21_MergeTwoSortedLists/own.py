from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        ret = merged
        merged.val = -1
        while list1 != None and list2!= None:
            if list1.val < list2.val:
                merged.next = list1
                merged, list1 = merged.next, list1.next
            else:
                merged.next = list2
                merged, list2 = merged.next, list2.next
        while list1 != None:
            merged.next = list1
            merged, list1 = merged.next, list1.next
        while list2 != None:
            merged.next = list2
            merged, list2 = merged.next, list2.next
        return ret.next
                
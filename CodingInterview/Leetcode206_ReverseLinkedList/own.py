# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        hptr = head
        ret = None
        rear = None
        while hptr != None:
            rear = ret
            ret = hptr
            hptr = hptr.next
            ret.next = rear
        return ret




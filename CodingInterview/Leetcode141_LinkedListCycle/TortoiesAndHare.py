# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        tortoise = head
        hare = head
        while tortoise != None and hare != None:
            tortoise = tortoise.next
            if tortoise == None:
                return False
            hare = hare.next
            if hare == None:
                return False
            hare = hare.next
            if tortoise == hare:
                return True
        return False

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c 
c.next = d
d.next = b

s = Solution()

print(s.hasCycle(a))
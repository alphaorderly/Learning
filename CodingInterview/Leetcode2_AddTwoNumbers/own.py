# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseLink(self, l):
        head = l
        pre, cur = None, head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def printNode(self, l):
        while l != None:
            print(l.val, end=' -> ')
            l = l.next
        print()

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        ans = None
        carry = 0
        while l1 != None and l2 != None:
            i = l1.val
            j = l2.val
            l1 = l1.next 
            l2 = l2.next
            sum = carry + i + j
            carry = sum // 10
            sum %= 10
            node = ListNode()
            node.val = sum
            node.next = ans
            ans = node

        while l1 != None:
            i = l1.val
            l1 = l1.next 
            sum = carry + i
            carry = sum // 10
            sum %= 10
            node = ListNode()
            node.val = sum
            node.next = ans
            ans = node

        while l2 != None:
            i = l2.val
            l2 = l2.next 
            sum = carry + i
            carry = sum // 10
            sum %= 10
            node = ListNode()
            node.val = sum
            node.next = ans
            ans = node
        
        if carry != 0:
            node = ListNode()
            node.val = carry
            node.next = ans
            ans = node

        return self.reverseLink(ans)
        

        
a = ListNode(2)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

d = ListNode(5)
e = ListNode(6)
f = ListNode(4)

d.next = e
e.next = f

s = Solution()

x = s.addTwoNumbers(a, d)

s.printNode(x)


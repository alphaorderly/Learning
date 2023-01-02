# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        hptr = head

        # 끝에 도달할때까지 검사.
        while hptr != None:
            if hptr.child == None:
                hptr = hptr.next

            # child가 존재할 경우 Flatten 해줍니다.
            # flatten 이후 다음 hptr은 child의 첫번째 Node를 가리키게 됩니다.
            # 자연스럽게 child도 flatten 하게 됩니다.
            else:
                # 다음 값 미리 저장해놓기
                next = hptr.next

                # 옆에 child 붙히기
                hptr.next = hptr.child
                hptr.child.prev = hptr

                # 마지막 찾기
                last = hptr.child
                while last.next != None:
                    last = last.next

                # 마지막도 붙히기
                last.next = next
                if next != None:
                    next.prev = last

                hptr.child = None

                hptr = hptr.next

        return head

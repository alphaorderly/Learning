# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root:'Node') -> List[int]:
        ans = []
        def postorder(root: 'Node'):
            if root != None:
                for c in root.children:
                    postorder(c)
                ans.append(root.val)
        postorder(root)
        return ans
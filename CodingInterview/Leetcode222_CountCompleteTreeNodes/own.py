# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count(root: Optional[TreeNode]):
    if root == None: return 0;
    return count(root.left) + count(root.right) + 1
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return count(root)
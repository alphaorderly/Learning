from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validity(root: Optional[TreeNode], lowerBound: int, upperBound: int):
    if root == None: return True
    if root.val <= lowerBound or root.val >= upperBound: return False
    return validity(root.left, lowerBound, root.val) and validity(root.right, root.val, upperBound)
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return validity(root, -(2**32-1), 2**32)
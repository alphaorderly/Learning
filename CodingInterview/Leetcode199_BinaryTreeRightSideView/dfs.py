# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Optional[TreeNode], ans, level: int = 0):
    if len(ans) <= level: ans.append(root.val)
    if root.right != None:
        dfs(root.right, level + 1)
    if root.left != None:
        dfs(root.left, level + 1)
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        ans = []
        dfs(root, ans)
        return ans

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LevelNode:
    def __init__(self, node: TreeNode, level: int):
        self.node = node
        self.level = level
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        
        // 루트 노드를 집어 넣고 시작
        q = [ LevelNode(root, 0) ]

        ans = dict()

        while len(q) != 0:
            node = q[0]
            q.pop(0)
            if node.level not in ans:
                ans[node.level] = list()
            ans[node.level].append(node.node.val)
            if node.node.left != None:
                // 자식 노드는 레벨 1 증가
                q.append(LevelNode(node.node.left, node.level + 1))
            if node.node.right != None:
                q.append(LevelNode(node.node.right, node.level + 1))

        ret = []
        for i in range(10000):
            if i not in ans: break
            ret.append(ans[i])

        return ret
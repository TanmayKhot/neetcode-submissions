# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
            
        d = {}
        q = deque()

        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if level in d:
                d[level].append(node.val)
            else:
                d[level] = [node.val]

            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        
        res = []
        for i in range(len(d)):
            res.append(d[i])
        
        return res
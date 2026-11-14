# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        res = 0

        stack = [(root, root.val)]

        while stack:
            node, m = stack.pop()
            if node.val >= m:
                res += 1
        
            maxi = max(m, node.val)

            if node.left: stack.append((node.left, maxi))
            if node.right: stack.append((node.right, maxi))
     
        return res
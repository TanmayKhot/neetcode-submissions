# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        
        def backtrack(node, target, path):

            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            if backtrack(node.left, target, path) or backtrack(node.right, target, path):
                return True
            
            path.pop()

            return False

        pathp = []
        pathq = []

        backtrack(root, p, pathp)
        backtrack(root, q, pathq)

        i = 0
        l = min(len(pathp), len(pathq))

        while i < l and pathp[i] == pathq[i] :
            i += 1
    

        return pathp[i-1]

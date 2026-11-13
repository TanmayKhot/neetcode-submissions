# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def valid(node, p, q):

            if node.val >= p and node.val <= q:
                return node
            
            if node.val > q:
                return valid(node.left, p, q)
            
            if node.val < p:
                return valid(node.right, p, q)
        
        if not root:
            return None

        pp = min(p.val , q.val)
        qq = max(p.val, q.val)

        return valid(root, pp, qq)
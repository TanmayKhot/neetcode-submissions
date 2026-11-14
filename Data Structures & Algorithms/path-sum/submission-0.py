# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, sum = stack.pop()
            sum += node.val

            if not node.left and not node.right and sum == targetSum:
                return True
            
            if node.left: stack.append((node.left,sum))
            if node.right: stack.append((node.right, sum))
        
        return False
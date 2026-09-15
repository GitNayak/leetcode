# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countFrom(node, remaining):
            if not node:
                return 0
            
            count = 0
            
            if node.val == remaining:
                count = 1
            
            count += countFrom(node.left, remaining - node.val)
            count += countFrom(node.right, remaining - node.val)
            
            return count
        
        def countAll(node):
            if not node:
                return 0
            
            return (
                countFrom(node, targetSum)
                + countAll(node.left)
                + countAll(node.right)
            )
        
        return countAll(root)
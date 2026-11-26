# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def check(root,lo,hi):
            if root is None:
                return True
            if lo<root.val<hi:
                left=check(root.left,lo,root.val)
                right=check(root.right,root.val,hi)
                return left and right
            return False
        
        return check(root,float('-inf'),float('inf'))


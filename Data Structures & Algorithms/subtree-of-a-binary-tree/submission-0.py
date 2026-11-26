# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(root1,root2):
            if (root1 is None and root2 is None):
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            left=compare(root1.left,root2.left)
            right=compare(root1.right,root2.right)
            return left and right and root1.val==root2.val
        
        def find(root,subroot):
            if not root:
                return False
            if root.val==subroot.val:
                if compare(root,subroot):
                    return True
            left=find(root.left,subroot)
            right=find(root.right,subroot)
            return left or right

        return find(root,subRoot)

        
        
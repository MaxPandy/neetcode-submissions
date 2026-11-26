# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root,node,path):
           
            path.append(root)
            if root.val>node.val:
                path=search(root.left,node,path)
            elif root.val<node.val:
                path=search(root.right,node,path)
            return path
        p1,p2=search(root,p,[]),search(root,q,[])
        for i in range(min(len(p1),len(p2))):
            if p1[i]!=p2[i]:
                return p1[i-1]
        return p1[min(len(p1),len(p2))-1]

            
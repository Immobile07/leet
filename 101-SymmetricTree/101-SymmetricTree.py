# Last updated: 4/4/2026, 12:42:32 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self,root):
        if root==None:
            return [None]
        else:
            l=self.path(root.left)
            r=self.path(root.right)
            md=[root.val]
            md+=l+r
            return md

    def path2(self,root):
        if root==None:
            return [None]
        else:
            l=self.path2(root.right)
            r=self.path2(root.left)
            md=[root.val]
            md+=l+r
            return md
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if len(self.path(root.left))!=len(self.path2(root.right)):
            return False
        else:
            x=self.path(root.left)
            y=self.path2(root.right)
            for i in range (len(x)):
                if x[i]!=y[i]:
                    return False
            return True
# Last updated: 4/4/2026, 12:42:23 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else:
            l=self.minDepth(root.left)
            r=self.minDepth(root.right)
            if l==0:
                return r+1
            elif r==0:
                return l+1
            else:
                if l>r:
                    return r+1
                else:
                    return l+1
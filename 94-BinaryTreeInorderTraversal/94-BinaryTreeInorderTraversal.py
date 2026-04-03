# Last updated: 4/4/2026, 12:42:36 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        else:
            lr=[]
            l=self.inorderTraversal(root.left)
            if l!=[]:
                lr+=l
            lr.append(root.val)
            r=self.inorderTraversal(root.right)
            
            if r!=[]:
                lr+=r
            return lr
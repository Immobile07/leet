# Last updated: 4/4/2026, 12:42:17 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        else:
            lr=[]
            l=self.postorderTraversal(root.left)
            if l!=[]:
                lr+=l
            r=self.postorderTraversal(root.right)
            if r!=[]:
                lr+=r
            lr.append(root.val)
            return lr
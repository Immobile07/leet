# Last updated: 4/4/2026, 12:42:20 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        else:
            lr=[]
            lr.append(root.val)
            l=self.preorderTraversal(root.left)
            r=self.preorderTraversal(root.right)

            if l!=[]:
                lr+=l
            if r!=[]:
                lr+=r
        return lr
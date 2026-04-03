# Last updated: 4/4/2026, 12:42:27 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def cnvrt(arr,l,r):
        if l>r:
            return 
        else:
            root=TreeNode(arr[(l+r)//2])
            root.left=cnvrt(arr,l,((l+r)//2)-1)
            root.right=cnvrt(arr,((l+r)//2)+1,r)
            return root
class Solution:
    

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        else:
            return cnvrt(nums,0,len(nums)-1)
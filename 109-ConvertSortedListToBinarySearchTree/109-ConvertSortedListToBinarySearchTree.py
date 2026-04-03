# Last updated: 4/4/2026, 12:42:25 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lst(head):
    ls=[]
    temp=head
    while(temp!=None):
        ls.append(temp.val)
        temp=temp.next
    return ls
def tree(lsr,l,r):
    if l>r:
        return
    else:
        mid=(l+r)//2
        root=TreeNode(lsr[mid])
        root.left=tree(lsr,l,mid-1)
        root.right=tree(lsr,mid+1,r)
        return root
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        ls2=lst(head)
        return tree(ls2,0,len(ls2)-1)

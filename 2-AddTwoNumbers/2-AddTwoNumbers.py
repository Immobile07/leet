# Last updated: 9/13/2025, 4:05:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1=''
        st2=''
        tmp1=l1
        tmp2=l2
        while(l1!=None):
            st1=str(l1.val)+st1
            l1=l1.next
        while(l2!=None):
            st2=str(l2.val)+st2
            l2=l2.next
        
        st3=str(int(st2)+int(st1))
        st3="".join(reversed(st3))
        ln=len(st3)
        l3=None
        tmp3=None
        for i in range(ln):
            if i==0:
                l3=ListNode(int(st3[i]))
                tmp3=l3
            else:
                nw=ListNode(int(st3[i]))
                tmp3.next=nw
                tmp3=tmp3.next
        return l3
            
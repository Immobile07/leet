# Last updated: 9/27/2025, 11:23:57 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ln=len(lists)
        if ln==0:
            return None
        hr=None
        st=-1
        start=-1
        for i in range(ln):
            if st!=-1 and lists[i]!=None:
                if hr.val>lists[i].val:
                    hr=lists[i]
                    st=i
            elif lists[i]!=None:
                hr=lists[i]
                st=i
                start=i
        
        if st==start:
            for i in range(st+1,ln):
                tmp1=hr
                tmp2=lists[i]
                while(tmp1!=None and tmp2!=None):
                    if tmp2.val<=tmp1.val:
                        smt1=tmp1.next
                        tmp1.next=tmp2
                        tmp2=tmp2.next
                        tmp1.next.next=smt1
                    elif tmp1.next!=None and tmp1.val<tmp2.val<tmp1.next.val:
                        smt1=tmp1.next
                        tmp1.next=tmp2
                        tmp2=tmp2.next
                        tmp1.next.next=smt1
                    else:
                        tmp1=tmp1.next
                if tmp1==None and tmp2!=None:
                    tm3=hr
                    while(tm3.next!=None):
                        tm3=tm3.next
                    tm3.next=tmp2
            return hr
        else:
            for i in range(st-1,start-1,-1):
                tmp1=hr
                tmp2=lists[i]
                while(tmp1!=None and tmp2!=None):
                    if tmp2.val<=tmp1.val:
                        smt1=tmp1.next
                        tmp1.next=tmp2
                        tmp2=tmp2.next
                        tmp1.next.next=smt1
                    elif tmp1.next!=None and tmp1.val<tmp2.val<tmp1.next.val:
                        smt1=tmp1.next
                        tmp1.next=tmp2
                        tmp2=tmp2.next
                        tmp1.next.next=smt1
                    else:
                        tmp1=tmp1.next
                if tmp1==None and tmp2!=None:
                    tm3=hr
                    while(tm3.next!=None):
                        tm3=tm3.next
                    tm3.next=tmp2
            for i in range(st+1,ln):
                    tmp1=hr
                    tmp2=lists[i]
                    while(tmp1!=None and tmp2!=None):
                        if tmp2.val<=tmp1.val:
                            smt1=tmp1.next
                            tmp1.next=tmp2
                            tmp2=tmp2.next
                            tmp1.next.next=smt1
                        elif tmp1.next!=None and tmp1.val<tmp2.val<tmp1.next.val:
                            smt1=tmp1.next
                            tmp1.next=tmp2
                            tmp2=tmp2.next
                            tmp1.next.next=smt1
                        else:
                            tmp1=tmp1.next
                    if tmp1==None and tmp2!=None:
                        tm3=hr
                        while(tm3.next!=None):
                            tm3=tm3.next
                        tm3.next=tmp2

            return hr
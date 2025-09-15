# Last updated: 9/15/2025, 7:30:10 PM
class Solution:
    def reverse(self, x: int) -> int:
        if x< (-2**31) or x> (2**31)-1:
            return 0
        if x<0:
            st=str(x)
            st=st[::-1]
            z= int("-"+st[:-1])
            if z< (-2**31) or z> (2**31)-1:
                return 0
            else:
                return z
        else:
            st=str(x)
            st=int(st[::-1])
            
            if st< (-2**31) or st> (2**31)-1:
                return 0
            else:
                return st
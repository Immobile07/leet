# Last updated: 9/13/2025, 1:30:00 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st=''
        for i in digits:
            st+=str(i)
        st=str(int(st)+1)
        nw=[]
        for i in st:
            nw.append(int(i))
        return nw
        
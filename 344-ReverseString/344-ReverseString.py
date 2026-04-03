# Last updated: 4/4/2026, 12:41:46 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        z=len(s)
        i=0
        j=z-1
        while(i<=j):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
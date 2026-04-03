# Last updated: 4/4/2026, 12:41:43 AM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        trck=0
        for i in range(len(s)):
            fnd=False
            for j in range(trck,len(t)):
                if s[i]==t[j]:
                    fnd=True
                    trck=j+1
                    break
            if fnd==False:
                return False
        return True
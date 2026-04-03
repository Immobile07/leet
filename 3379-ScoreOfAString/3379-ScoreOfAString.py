# Last updated: 4/4/2026, 12:41:10 AM
class Solution:
    def scoreOfString(self, s: str) -> int:
        ln=len(s)
        sm=0
        for i in range(ln-1):
            sm+=abs(ord(s[i])-ord(s[i+1]))
        return sm
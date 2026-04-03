# Last updated: 4/4/2026, 12:42:15 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        st=""
        tmp=""
        s=s.rstrip()
        s=s.lstrip()
        for i in range(len(s)-1,-1,-1):
            if i==0:
                tmp+=s[i]
                st+=inv(tmp)
            if s[i]==" " and s[i+1]!=" ":
                st+=inv(tmp)
                st+=" "
                tmp=""
            elif (s[i]>='a' and s[i]<='z') or (s[i]>="A" and s[i]<="Z") or(s[i]>='0' and s[i]<="9"):
                tmp+=s[i]
        return st
def inv(s):
    tr=""
    for i in range(len(s)-1,-1,-1):
        tr+=s[i]
    return tr
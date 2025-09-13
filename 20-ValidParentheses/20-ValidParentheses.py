# Last updated: 9/13/2025, 3:59:58 PM
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="(" or i=="{" or  i=="[":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                else:
                    r=st.pop(-1)
                    if (i==")" and r!="(") or (r!="{" and i=="}") or (r!='[' and i==']'):
                        return False
        else:
            if len(st)==0:
                return True
            else:
                return False
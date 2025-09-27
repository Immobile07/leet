# Last updated: 9/27/2025, 11:23:52 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1={}
        for i in s:
            if i not in dct1.keys():
                dct1[i]=1
            else:
                dct1[i]+=1
        dct2={}
        for i in t:
            if i not in dct2.keys():
                dct2[i]=1
            else:
                dct2[i]+=1
        for i in dct2.keys():
            if i not in dct1.keys():
                return False
            else:
                if dct1[i]!=dct2[i]:
                    return False
        if len(s)!=len(t):
            return False
        return True
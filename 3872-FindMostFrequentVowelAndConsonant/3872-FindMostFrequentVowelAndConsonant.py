# Last updated: 9/13/2025, 4:05:16 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowl=['a','e','i','o','u']
        dc_v={}
        dc_c={}
        for i in s:
            if i in vowl:
                if i not in dc_v.keys():
                    dc_v[i]=1
                else:
                    dc_v[i]+=1
            else:
                if i not in dc_c.keys():
                    dc_c[i]=1
                else:
                    dc_c[i]+=1
        
        mx=0
        for i in dc_v.values():
            if i>=mx:
                mx=i

        mx2=0
        for j in dc_c.values():
            if j>=mx2:
                mx2=j
        return mx+mx2
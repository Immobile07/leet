# Last updated: 10/3/2025, 12:08:45 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        for i in nums:
            if i not in dct.keys():
                dct[i]=1
            else:
                dct[i]+=1
        vst={}
        for i in dct.keys():
            vst[i]=False
        mx=[]
        for i in range(k):
            maxi=float('-inf')
            ind=None
            for k,v in dct.items():
                if v>=maxi and vst[k]==False:
                    maxi=v
                    ind=k
            
            mx.append(ind)
            vst[ind]=True
        return mx
                    
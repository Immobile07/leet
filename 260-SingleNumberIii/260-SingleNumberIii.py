# Last updated: 4/4/2026, 12:41:55 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        frst={}
        for i in range(len(nums)):
            if str(nums[i]) in frst.keys():
                frst[str(nums[i])]+=1
            else:
                frst[str(nums[i])]=1
        lr=[]
        for k in frst.keys():
            if frst[k]==1:
                lr.append(int(k))
        return lr
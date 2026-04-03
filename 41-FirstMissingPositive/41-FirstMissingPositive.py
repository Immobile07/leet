# Last updated: 4/4/2026, 12:42:47 AM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp={}
        fnd=False
        for i in range(len(nums)):
            if nums[i]>0:
                if nums[i] not in mp.keys():
                    mp[nums[i]]=1
        for i in range(1,len(nums)+1):
            if i not in mp.keys():
                return i
        if fnd==False:
            return len(nums)+1
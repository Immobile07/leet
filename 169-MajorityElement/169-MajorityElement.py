# Last updated: 4/4/2026, 12:42:12 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr=0
        mjr=0
        for i in range(len(nums)):
            if nums[i]==curr:
                mjr+=1
            elif nums[i]!=curr and mjr==0:
                curr=nums[i]
                mjr+=1
            else:
                mjr-=1
        return curr
# Last updated: 4/4/2026, 12:41:16 AM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mn=nums[0]
            id=0
            for j in range(1,len(nums)):
                if mn>nums[j]:
                    id=j
                    mn=nums[j]
            nums[id]=mn*multiplier
        return nums

# Last updated: 9/27/2025, 11:23:56 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nm=[]
        for i in range(len(nums)):
            if nums[i] not in nm:
                nm.append(nums[i])
            else:
                nums[i]="_"

        for i in range(len(nm)):
            nums[i]=nm[i]
        
        return len(nm)
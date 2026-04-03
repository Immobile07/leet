# Last updated: 4/4/2026, 12:41:49 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=len(nums)
        z=x-1
        for i in range(x-1):
            if nums[i]==0:
                for j in range(i+1,x):
                    if nums[j]!=0:
                        nums[j],nums[i]=nums[i],nums[j]
                        break
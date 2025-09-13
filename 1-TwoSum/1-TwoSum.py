# Last updated: 9/13/2025, 1:37:06 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln=len(nums)-1
        for i in range(ln):
            for j in range(i+1,ln+1):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
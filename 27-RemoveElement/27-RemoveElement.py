# Last updated: 4/4/2026, 12:42:49 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]="_"
                cnt+=1
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]=="_" and nums[j+1]!="_":
                    nums[j]=nums[j+1]
                    nums[j+1]="_"
        return len(nums)-cnt
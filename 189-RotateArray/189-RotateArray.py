# Last updated: 4/4/2026, 12:42:08 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2=[]
        for i in range(len(nums)):
            nums2.append(nums[i])
        for i in range(len(nums)):
            nums[(i+k)%len(nums2)]=nums2[i]
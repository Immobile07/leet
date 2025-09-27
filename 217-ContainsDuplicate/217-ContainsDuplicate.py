# Last updated: 9/27/2025, 11:23:51 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct={}
        for i in nums:
            if i not in dct.keys():
                dct[i]=1
            else:
                return True
        return False
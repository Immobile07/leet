# Last updated: 12/7/2025, 1:14:38 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nm=[]
        nm2=[]
        nm3=[]
        l=len(nums)
        for i in range(l):
            if i==0:
                nm.append(1)
            else:
                nm.append(nm[i-1]*nums[i-1])
        for i in range(l-1,-1,-1):
            if i==l-1:
                nm2.append(1)
            else:
                nm2.append(nm2[-1]*nums[i+1])
        nm2=nm2[::-1]
        for i in range(l):
            nm3.append(nm[i]*nm2[i])
        return nm3
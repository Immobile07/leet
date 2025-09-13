# Last updated: 9/13/2025, 4:21:20 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1==[] and nums2==[]:
            return []
        def merge(nm2,nm3):
            i=0
            j=0
            ln2=len(nm2)
            ln3=len(nm3)
            nm4=[]
            while(i<ln2 and j<ln3):
                if nm2[i]<nm3[j]:
                    nm4.append(nm2[i])
                    i+=1
                else:
                    nm4.append(nm3[j])
                    j+=1
            while (i<ln2):
                nm4.append(nm2[i])
                i+=1
            while (j<ln3):
                nm4.append(nm3[j])
                j+=1
            return nm4
        def divide(nm1):
            if len(nm1)==1:
                return nm1
            dvd=len(nm1)//2
            lft=divide(nm1[:dvd])
            right=divide(nm1[dvd:])
            return merge(lft,right)
        nm_sm=nums1+nums2
        nm=divide(nm_sm)
        if len(nm)%2!=0:
            return nm[(len(nm)-1)//2]
        else:
            ln=len(nm)
            return (nm[ln//2]+ nm[(ln//2)-1])/2

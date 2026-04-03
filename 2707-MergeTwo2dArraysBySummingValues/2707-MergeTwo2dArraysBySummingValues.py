# Last updated: 4/4/2026, 12:41:15 AM
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
            i=0
            j=0
            arr=[]
            while(i<len(nums1) and j<len(nums2)):
                if nums1[i][0]==nums2[j][0]:
                    ls=[nums1[i][0],nums1[i][1]+nums2[j][1] ]
                    arr.append(ls)
                    i+=1
                    j+=1
                else:
                    if nums1[i][0]>nums2[j][0]:
                        arr.append(nums2[j])
                        j+=1
                    else:
                        arr.append(nums1[i])
                        i+=1
            while(i<len(nums1)):
                arr.append(nums1[i])
                i+=1
            while(j<len(nums2)):
                arr.append(nums2[j])
                j+=1
            return arr
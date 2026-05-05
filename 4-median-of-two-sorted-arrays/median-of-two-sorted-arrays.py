class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        m=len(nums3)
        if m%2!=0:
            idx=(m+1)//2
            return nums3[idx-1]
        else:
            idx1=m//2
            idx2=(m//2)+1
            return (nums3[idx1-1]+nums3[idx2-1])/2
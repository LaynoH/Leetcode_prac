class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1+nums2
        merge.sort()

        median = 0.0
        if len(merge)%2==0:
            median = (merge[len(merge)//2-1]+merge[len(merge)//2])/2
        else:
            median = (merge[len(merge)//2])
        return median    

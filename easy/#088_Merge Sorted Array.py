class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp1 = nums1[:m]
        tmp2 = nums2[:n] 
        loop = m+n
        
        for i in range(loop):
            if len(tmp1) and ((len(tmp2) and tmp1[0]<=tmp2[0]) or len(tmp2)==0):
                nums1[i] = tmp1.pop(0)
            elif len(tmp2):
                nums1[i] = tmp2.pop(0)
        
        

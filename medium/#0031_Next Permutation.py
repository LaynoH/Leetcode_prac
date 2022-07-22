class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        # find index of decreasing element (nums[i-1]>nums[i] & nums[i]<nums[i+1])
        while i>=0 and nums[i+1]<=nums[i]:
            i-=1
        
        # find element just larger than decreasing element
        j = len(nums)-1
        if i>=0:
            # start from the end of list
            while nums[j]<=nums[i]:
                j-=1
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse elements after the decreasing element's index
        i+=1
        j = len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
            
# ref: solution            
            
     

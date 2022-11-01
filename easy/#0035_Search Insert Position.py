class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid=0
        
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0
        
        while low<=high:
            mid = low + (high - low)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid]>=target:
                high = mid-1
            else:
                low = mid+1
                
        if target>nums[mid]:
            return mid+1
        elif target<nums[mid]:
            return mid
        
# binary search
            

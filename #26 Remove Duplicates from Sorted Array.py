class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pivot = 0
        
        for i in range(len(nums)):
            if nums[pivot] != nums[i]:
                pivot+=1
                nums[pivot] = nums[i]
        return pivot+1

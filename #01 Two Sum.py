class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        for i in range(len(nums)):
            result = []
            if(target-nums[i]) in nums and nums.index(target-nums[i])!=i:
                result.append(i)
                result.append(nums.index(target-nums[i]))
                return result

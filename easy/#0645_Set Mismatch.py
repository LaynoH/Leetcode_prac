class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        err = -1
        corr = -1

        for i in range(1, len(nums)+1):
            if i not in nums:
                corr = i
            if nums.count(nums[i-1]) > 1:
                err = nums[i-1]
            if corr != -1 and err != -1:
                break
        return [err, corr]     
        

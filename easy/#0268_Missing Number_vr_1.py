class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxie = max(nums)

        for i in range(0, maxie):
            if i not in nums:
                return i
        return maxie+1
        

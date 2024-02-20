class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxie = max(nums)

        nums.sort()
        for i in range(0,maxie):
            if nums[i] != i:
                return i
        return maxie+1

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        subMax = subSum = nums[0]
        subMin = 0
        nums.pop(0)
        
        for i in nums:
            subMax = max(subMax+i, i)
            subMin = min(subMin+i, i)
            subSum = max(subSum, subMax, total-subMin)

        return subSum
      
# ref: https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/3066034/python3-dp-two-passes-for-beginners-with-explanations/

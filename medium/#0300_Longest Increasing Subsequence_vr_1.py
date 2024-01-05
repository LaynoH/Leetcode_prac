class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxL = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    maxL[i] = max(maxL[i], maxL[j] + 1)

        return max(maxL)

# ref: https://leetcode.com/problems/longest-increasing-subsequence/solutions/4509129/99-54-easy-solution-with-explanation/?envType=daily-question&envId=2024-01-05

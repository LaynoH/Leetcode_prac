class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #  window sliding method
        taken_bits = 0
        window_init = 0
        max_len = 0

        for window_end in range(len(nums)):
            while nums[window_end] & taken_bits != 0:
                taken_bits ^= nums[window_init]
                window_init += 1
            taken_bits |= nums[window_end]
            max_len = max(max_len, window_end-window_init+1)

        return max_len


        # ref https://leetcode.com/problems/longest-nice-subarray/editorial

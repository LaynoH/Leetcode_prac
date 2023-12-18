class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w = nums.pop(nums.index(max(nums)))
        x = nums.pop(nums.index(max(nums)))
        y = nums.pop(nums.index(min(nums)))
        z = nums.pop(nums.index(min(nums)))

        return (w * x) - (y * z)

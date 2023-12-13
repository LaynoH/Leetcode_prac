class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = nums.pop(nums.index(max(nums)))
        j = nums.pop(nums.index(max(nums)))
        return (i-1)*(j-1)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        toPair = list(zip(nums,nums[1:]))
        return all(i[0]>=i[1] for i in toPair) or all(i[0]<=i[1] for i in toPair)

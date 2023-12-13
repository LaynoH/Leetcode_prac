class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0 
        curr = 0
        while nums:
            curr = nums.pop(0)
            pair += nums.count(curr)
        return pair

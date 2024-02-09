class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1:set()}

        for i in sorted(nums):
            subsets[i] = max([subsets[j] for j in subsets if i%j==0], key = len)|{i}
            
        return (list(max(subsets.values(), key=len)))

# ref: https://leetcode.com/problems/largest-divisible-subset/solutions/4699827/short-and-easy-no-dp-no-recursion-python

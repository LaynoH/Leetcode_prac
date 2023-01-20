class Solution:
    def backtrace(self, i, sub, out, nums):
        if len(sub)>1:
            out.add(tuple(sub))
        if i==len(nums):
            return out
        if not sub or nums[i] >= sub[-1]:
            self.backtrace(i+1, sub+[nums[i]], out, nums)
        self.backtrace(i+1, sub, out, nums)
        return out

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        out = set()
        out = self.backtrace(0,[], out, nums)
        return out
      
# ref: https://leetcode.com/problems/non-decreasing-subsequences/solutions/3074787/python3-backtracking-for-beginners/

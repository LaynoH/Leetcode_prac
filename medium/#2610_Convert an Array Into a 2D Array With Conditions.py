class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        len2D = 0
        for i in list(set(nums)):
            len2D = max(len2D, nums.count(i))    

        res = [[] for _ in range(len2D)]
        
        pivotI = 0
        for i in range(len(nums)):
            pivotI = 0
            while nums[i] in res[pivotI]:
                pivotI += 1
            res[pivotI].append(nums[i])
        return res

#check: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/4489526/better-than-100-c-java-python-javascript-2-approaches-explained/?envType=daily-question&envId=2024-01-02

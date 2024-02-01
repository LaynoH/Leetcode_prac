class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        if n % 3 != 0:
            return []
        res = []

        for i in range(0, n-2, 3):
            if (nums[i+2] - nums[i]) <= k:
                res.append([nums[i], nums[i+1], nums[i+2]])
            else:
                return []
        return res

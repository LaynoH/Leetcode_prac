class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        j, k = 0, 1
        for i in nums:
            if i>0:
                res[j] = i
                j += 2
            else:
                res[k] = i
                k += 2
        return (res)


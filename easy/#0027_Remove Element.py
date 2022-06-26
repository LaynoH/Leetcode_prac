class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        exist = nums.count(val)
        for i in range(exist):
            nums.remove(val)
        return len(nums)

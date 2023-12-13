class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r1 = list(filter(lambda x: x % 2 != 0, nums))
        r2 = list(filter(lambda x: x % 2 == 0, nums))
        return r2+r1

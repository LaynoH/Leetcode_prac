class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sortN = nums.copy()
        rsortN = nums.copy()
        sortN.sort()
        rsortN.sort(reverse=True)
        return (nums == sortN) or (nums == rsortN)

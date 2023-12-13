class Solution:
    def hammingWeight(self, n: int) -> int:
        oneB = 0
        while n!=0:
            oneB += (n%2)
            n >>= 1
        return oneB

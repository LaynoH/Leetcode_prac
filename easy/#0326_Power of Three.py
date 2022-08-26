class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= -(2**31) or n >= 2**31-1 or n == 0:
            return False
        
        while n/3 and n>1:
            n/=3
        
        if n==1:
            return True
        return False
